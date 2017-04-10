# -*- coding: utf-8 -*-

from openerp import models, fields, api


class hr_employee(models.Model):
    _inherit = 'hr.employee'

    employee_code = fields.Char(string='Employee Code', required=True, help="Employee Code", index=True)

    ext_no = fields.Char(string='Extension Number')

    notes_id = fields.Char(string='Notes ID')

    eng_name = fields.Char(string='English Name')

    approval_level_id = fields.Many2one('hrm.approval_level',
                                        ondelete='set null',
                                        string='Approval Level',
                                        required=False)

    grade_id = fields.Many2one('hrm.grade',
                               ondelete='set null',
                               string='Grade Name',
                               required=False)

    arrival_date = fields.Date(string='Arrival Date')

    quit_date = fields.Date(string='Quit Date')

    blood_type = fields.Selection([('A', 'A'), ('B', 'B'), ('O', 'O'), ('AB', 'AB')], 'Blood Type')

    sap_emp_code = fields.Char(string='SAP Employee Code')

    department_code = fields.Char(related='department_id.department_code', store=False)

    department_name = fields.Char(related='department_id.name', store=False)

    job_agent_id = fields.Many2one('hr.employee',
                               ondelete='set null',
                               string='Job Agent',
                               required=False)

    approval_agent_id = fields.Many2one('hr.employee',
                               ondelete='set null',
                               string='Approval Agent',
                               required=False)

    approval_agent_mode = fields.Selection([('A', 'According to system'), ('M', 'Manual')], 'Approval Agent Mode')

    approval_agent_status = fields.Selection([('A', 'Activated'), ('D', 'Deactivated')], 'Approval Agent Status',
                                             default='D')

    _sql_constraints = [
        ('employee_code_unique',
         'UNIQUE(employee_code)',
         "The Employee Code must be unique"),
    ]
