# -*- coding: utf-8 -*-

from openerp import models, fields, api


class hr_approval_level(models.Model):
    _name = 'hrm.approval_level'

    approval_level_code = fields.Integer(string="Approval Level Code", required=True, index=True)

    name = fields.Char(string='Approval Level Name', required=True)

    complete_name = fields.Char(string="Approval Level", compute='_get_complete_name', store=True)

    _rec_name = 'complete_name'

    @api.depends('approval_level_code', 'name')
    def _get_complete_name(self):
        for r in self:
            r.complete_name = '%s %s' % (r.approval_level_code, r.name)

    _sql_constraints = [
        ('approval_level_code_unique',
         'UNIQUE(approval_level_code)',
         "The Approval Level Code must be unique"),
    ]
