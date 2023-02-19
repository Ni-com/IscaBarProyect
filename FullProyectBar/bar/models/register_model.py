import random
from odoo import models, fields, api


#from datetime import datetime, timedelta

class RegisterModel(models.Model):
     _name = 'bar.register_model'
     _description = 'Register Model'



     quantity = fields.Integer("Quantity",default=1)
     order = fields.Many2one("bar.order_model",string="Order", ondelete="cascade")
     product = fields.Many2one("bar.product_model",string="Product")
     anotation=fields.Text("Anotations")

     state = fields.Selection(string="Status",selection=[('P','Pending'),('C','Completed'),('D','Delivered'),('F','Finished')], default="P")
     location = fields.Selection(string="Location",selection=[('K','Kitchen'),('B','Barman'),('W','Waiter')], store=True)
     location_related = fields.Selection(string="Location (related)", related="location", store=True)

     @api.onchange('product')
     def _onchange_product(self):
          if self.product:
               if 6 in self.product.category.ids:
                    self.location = 'B'
               else:
                    self.location = 'K'     

     def cookerStatus(self):
          self.ensure_one()
          if self.state == "P":
               self.state = "C"
          self.location = "W"
          
          return {
               'name': ('Cooker Window'),
               'view_type': 'form',
               'view_mode': 'kanban,form',
               'res_model': 'bar.register_model',
               'views': [(self.env.ref('bar.register_model_kanban').id,'kanban'),(self.env.ref('bar.register_model_form_cooker').id,'form')],
               'view_id': False,
               'domain': [('state', '=', 'P'), ('location_related', '=', 'K')],
               'type': 'ir.actions.act_window',
               'target': 'current',
               'nodestroy': True
          }
     
     def barmanStatus(self):
          self.ensure_one()
          if self.state == "P":
               self.state = "C"
          self.location = "W"
          return {
               'name': ('Barman Window'),
               'view_type': 'form',
               'view_mode': 'kanban,form',
               'res_model': 'bar.register_model',
               'views': [(self.env.ref('bar.register_model_kanban').id,'kanban'),(self.env.ref('bar.register_model_form_barman').id,'form')],
               'view_id': False,
               'domain': [('state', '=', 'P'), ('location_related', '=', 'B')],
               'type': 'ir.actions.act_window',
               'target': 'current',
               'nodestroy': True
          }
         

     def waiterStatus(self):
          self.ensure_one()
          if self.state == "P" or self.state == "C":
               self.state = "D"
          return {
               'name': ('Waiter Window'),
               'view_type': 'form',
               'view_mode': 'tree,form',
               'res_model': 'bar.register_model',
               'views': [(self.env.ref('bar.register_model_list').id,'tree'),(self.env.ref('bar.register_model_form_waiter').id,'form')],
               'view_id': False,
               'domain': [('state', '!=', 'D'), ('state', '!=', 'F')],
               'type': 'ir.actions.act_window',
               'target': 'current',
               'nodestroy': True
          }
     
     def waiterStatusTree(self):
          self.ensure_one()
          if self.state == "P" or self.state == "C":
               self.state = "D"
          
     
     def show_notification(self):
          self.env.user.notify_success(message='My success message')
          

     