# test_info.py
# Copyright (c) 2024, Aman and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase

class TestInfo(FrappeTestCase):

    def setUp(self):
        self.doc = frappe.get_doc({
            'doctype': 'Info',
            'name1': 'Aman G',
            'age': 22,
            'number': '9876543210'
        })
        self.doc.insert()
        frappe.db.commit()


    def tearDown(self):
        if self.doc.name:
            frappe.delete_doc('Info', self.doc.name)
            frappe.db.commit()

    def test_field(self):
        doc2 = frappe.get_doc("Info", self.doc.name)
        self.assertEqual("Aman G", doc2.name1)
        self.assertEqual(22, int(doc2.age))
        self.assertNotEqual('32222222',doc2.number)

    def test_update(self):
        doc2 = frappe.get_doc("Info", self.doc.name)
        doc2.update({
            'age': 31
        })
        frappe.db.commit()
        self.assertEqual(31,int(doc2.age))



