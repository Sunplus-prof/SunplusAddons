# -*- coding: utf-8 -*-
{
    'name': "HRM",

    'summary': """
        This module extends the default hr module for customization.""",

    'description': """
        This module extends the default hr module for customization.
    """,

    'author': "Stan Hotchner",
    'website': "http://www.sunplus.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Human Resources',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'views/views.xml',
        'views/grade.xml',
        'views/employee.xml',
        'views/department.xml',
        'views/approval_level.xml',
        'demo.xml'

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}