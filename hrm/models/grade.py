# -*- coding: utf-8 -*-

from openerp import models, fields, api


class Grade(models.Model):
    _name = 'hrm.grade'

    grade_code = fields.Char(string='Grade Code', required=True, help="Grade Code", index=True)

    name = fields.Char(string='Grade Name', required=True, help="Grade", index=True)

    complete_name = fields.Char(
        string="Grade Level", compute='_get_complete_name', store=True)

    _rec_name = 'complete_name'

    @api.depends('grade_code', 'name')
    def _get_complete_name(self):
        for r in self:
            r.complete_name = '%s %s' % (r.grade_code, r.name)

    _sql_constraints = [
        ('grade_id_unique',
         'UNIQUE(grade_code)',
         "The Grade Code must be unique"),
    ]
