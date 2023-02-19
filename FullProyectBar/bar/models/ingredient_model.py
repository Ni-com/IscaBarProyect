import random
from odoo import models, fields, api
#from datetime import datetime, timedelta

class IngredientModel(models.Model):
    _name = 'bar.ingredient_model'
    _description = 'ingredient Model'



    name = fields.Char("Ingredient", required=True)
    nutritionalValue= fields.Char("Nutritional Value")
    allergies=fields.Char("Allergies")
    products = fields.Many2many("bar.product_model",string="Products")
    