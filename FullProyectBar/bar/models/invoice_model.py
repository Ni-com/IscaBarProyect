from odoo import models, fields, api
from datetime import datetime, timedelta
from odoo.exceptions import ValidationError

class InvoiceModel(models.Model):
    _name = 'bar.invoice_model'
    _description = 'Invoice Model'
    

    name = fields.Integer(string="Ref",required=True,default=lambda self: self._get_id(),index=True)
    date = fields.Date(string="Date",required=True,default=datetime.now(),help="Date")
    pay=fields.Monetary("Base ",compute="_total", store=True)
    vat = fields.Selection(string="VAT",selection=[('0','0'),('4','4'),('10','10'),('21','21')], default='10',help="IVA")
    lines = fields.One2many("bar.invoicelines_model","invoice",string="Lines")
    client=fields.Char("Client")
    currency_id=fields.Many2one("res.currency",string="Currency", default=lambda self:self.env.user.company_id.currency_id)
    total = fields.Float(string="Total",compute="_completeprice",help="Total invoice",store=True)
    
    state = fields.Selection(string="Status",selection=[('D','Draft'),('C','Confirmed')], default="D")

    @api.depends("lines.product.price","lines.quantity")
    def _total(self):
        self.pay=0
        for rec in self.lines:
            self.pay += (rec.quantity * rec.product.price)

    def _get_id(self):
          if len(self.env['bar.invoice_model'].search([])) == 0:
               return 1
          return (self.env['bar.invoice_model'].search([])[-1].id + 1)

    @api.depends("pay", "vat")
    def _completeprice(self):
        self.total = self.pay*int(self.vat)/100.0 + self.pay

    def confirmInvoice(self):
          self.ensure_one()
          self._cr.autocommit(False)
          if self.state == "D":
               self.state = "C"
          self._cr.commit()
          self._cr.autocommit(True)
          return True
    
    #def print_invoice(self):
        #return self.env.ref('report_invoice_model').report_action(self)
