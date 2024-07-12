from odoo import api, fields, models, _
class UserDepartment(models.Model):
    _name = "user.department"
    _description = 'User Department'
    
    name = fields.Char(string="Department", required=True)