# -*- coding: utf-8 -*-

from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError
from psycopg2 import IntegrityError

class TestModelA(TransactionCase):
    def setUp(self):
        super(TestModelA, self).setUp()
        self.grade = self.env['hrm.grade']

    def test_grade_not_duplicate_grade_code(self):
        record = self.grade.create({'grade_code': '00B', 
                                    'name': 'capten',})
                                    
        with self.assertRaises(IntegrityError):
            record = self.grade.create({'grade_code': '00B',
                                        'name': 'capten',})
    
    def test_grade_name_is_not_NULL(self):
        with self.assertRaises(IntegrityError):
            record = self.grade.create({'grade_code': '00B',}) #name字段给空值
            
    def test_grade_name_is_not_empty(self):
        with self.assertRaises(ValidationError):
            record = self.grade.create({'grade_code': '00B', 
                                        'name': '',})
        '''
        print(record.name)
        self.assertEqual(
            record.name,
            'capten')
        '''