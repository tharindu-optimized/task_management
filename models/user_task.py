from odoo import api, fields, models, _

class UserTask(models.Model):
    _name = "user.task"
    _description = 'Task'
    
    name = fields.Char(string="Task", required=True)