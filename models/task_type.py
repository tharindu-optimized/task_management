from odoo import api, fields, models, _


class TaskType(models.Model):
    _name = "task.type"
    _description = 'Task Type'

    name = fields.Char(string="Task", required=True)
