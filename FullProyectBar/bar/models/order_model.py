import random
from odoo import models, fields, api
from odoo.exceptions import ValidationError
#from datetime import datetime, timedelta

class OrderModel(models.Model):
    _name = 'bar.order_model'
    _description = 'Order Model'
   
    name = fields.Integer("Table")
    client=fields.Char("Client")
    pax=fields.Integer("Pax",default=1)
    waiter=fields.Char("Waiter name", default="Waiter")
    register = fields.One2many("bar.register_model","order",string="Registration")
    aditionalData=fields.Char("Aditional Data", default="No")
    currency_id=fields.Many2one("res.currency",string="Currency", default=lambda self:self.env.user.company_id.currency_id)
    pay=fields.Monetary("Pay ",compute="_total", store=True)
    state = fields.Selection(string="Status",selection=[('D','Draft'),('C','Confirmed')], default="D")
    deliverStatus=fields.Selection(string="WaiterStatus",selection=[('P','Pendent'),('A','AllDelivered')], compute="_compute_state")

    @api.depends('register.state')
    def _compute_state(self):
        for order in self:
            if all(reg.state == 'D' for reg in order.register):
                order.deliverStatus = 'A'
            else:
                order.deliverStatus = 'P'

    #Para hacer el grafico
    totalpay=fields.Monetary("Pay by table",compute="_totalPay", store=True)

    

    @api.onchange('name')
    def _onchange_name(self):
        self.client = 'Table {}'.format(self.name)

    @api.depends("register.product.price","register.quantity")
    def _total(self):
        self.pay=0
        for rec in self.register:
            self.pay += (rec.quantity * rec.product.price)

    @api.depends("pay")
    def _totalPay(self):
        self.totalpay=0
        for rec in self:
            self.totalpay += rec.pay

    def create_invoice(self):
        for rec in self:
            invoice_lines = []
            for line in rec.register:
                invoice_lines.append((0, 0, {'product': line.product.id, 'quantity': line.quantity}))
                line.write({'state': 'F'})
            invoice = {
                'client': rec.client,
                'pay': rec.pay,
                'lines': invoice_lines,
            }
            self.env['bar.invoice_model'].create(invoice)
            if self.state == "D":
               self.state = "C"
        return {
               'name': ('order List'),
               'view_type': 'form',
               'view_mode': 'tree,form',
               'res_model': 'bar.order_model',
               'domain': [('state', '=', 'D')],
               'type': 'ir.actions.act_window',
               'target': 'current',
               'nodestroy': True
        }

    