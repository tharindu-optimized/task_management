from odoo import api, fields, models, _

class Branch(models.Model):
    _name = "branch"
    _description = 'Branch'
    
    name = fields.Char(string="Branch", required=True)