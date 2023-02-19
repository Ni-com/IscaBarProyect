import random
from odoo import models, fields, api
#from datetime import datetime, timedelta

class CategoryModel(models.Model):
    _name = 'bar.category_model'
    _description = 'Category Model'
    _rec_name="complete_name"


    name = fields.Char("Category", required=True)
    description=fields.Char("description")
    products = fields.Many2many("bar.product_model",string="Products")
    parent_id = fields.Many2one("bar.category_model",string="Parent Category", ondelete="cascade")

    complete_name=fields.Char("Complete Name", compute="_compute_complete_name",recursive=True,store=True)

    @api.depends("name", "parent_id.complete_name")
    def _compute_complete_name(self):
        for category in self:
            if category.parent_id:
                category.complete_name='%s / %s' % (category.parent_id.complete_name, category.name)
            else:
                category.complete_name = category.name