from odoo import models, fields, api


class InvoiceLinesModel(models.Model):
    _name = 'bar.invoicelines_model'
    _description = 'Invoice Lines Model'



    quantity = fields.Integer("Quantity",default=1)
    invoice = fields.Many2one("bar.invoice_model",string="Invoice", ondelete="cascade")
    product = fields.Many2one("bar.product_model",string="Product")