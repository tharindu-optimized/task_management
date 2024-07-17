from odoo import api, fields, models, _

class TaskManagement(models.Model):
    _name = "task.management"
    # _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Task'

    name = fields.Char(string="AOT No", required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    date = fields.Datetime(string="Date", default=lambda self: fields.datetime.now(), readonly=True)
    due_date = fields.Date(string="Due Date")
    type_id = fields.Many2one('task.type', string="Type", required=True)
    assigned_to = fields.Many2one('res.users', string="Assigned To")
    in_ward = fields.Boolean(string="In Ward")
    outward = fields.Boolean(string="Outward")
    branch_id = fields.Many2one('branch', string="Branch")
    description = fields.Text(string="Description")
    status = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('approved', 'Approved'),
        ('hold', 'Hold on'),
        ('rejected', 'Rejected'),
        ('time_exceeded', 'Time Exceeded'),
    ], string="Status", default='draft')
    closing_date = fields.Date(string="Closing Date")
    closed_by = fields.Many2one('res.users', string="Closed By")


    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('task.name') or _('New')
        return super(TaskManagement, self).create(vals)
        
    def action_draft(self):
        self.status = 'draft'
        
    def action_confirmed(self):
        self.status = 'confirmed'
        
    def action_approve(self):
        self.status = 'approved'
        
    def action_reject(self):
        self.status = 'rejected'
        
    def action_hold(self):
        self.status = 'hold'
        
    def check_due_dates(self):
        today = fields.Date.today()
        overdue_tasks = self.search([('due_date', '<', today), ('status', '!=', 'time_exceeded')])
        overdue_tasks.write({'status': 'time_exceeded'})