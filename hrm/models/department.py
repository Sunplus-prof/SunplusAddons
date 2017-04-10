# -*- coding: utf-8 -*-

from openerp import models, fields


class hr_department(models.Model):
    _inherit = 'hr.department'
    _rec_name = 'name'

    department_code = fields.Char(string='Department Code', required=True, help="Department Code", index=True)

    department_eng_name = fields.Char(string='Department English Name', required=False)

    department_level = fields.Char(string='Department Level', required=True)
