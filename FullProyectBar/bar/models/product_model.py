import random
from odoo import models, fields, api
#from datetime import datetime, timedelta

class ProductModel(models.Model):
    _name = 'bar.product_model'
    _description = 'Product Model'



    name = fields.Char("Product", required=True)
    description=fields.Char("Description")
    photo = fields.Binary("Photo") 
    category = fields.Many2many("bar.category_model",string="Category")
    ingredients = fields.Many2many("bar.ingredient_model",string="Ingredients")
    stock = fields.Boolean("Stock", default=True)
    currency_id=fields.Many2one("res.currency",string="Currency", default=lambda self:self.env.user.company_id.currency_id)
    price = fields.Monetary(string="Price")

    