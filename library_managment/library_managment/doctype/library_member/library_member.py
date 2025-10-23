# Copyright (c) 2025, codeWithSwapnil and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class LibraryMember(Document):
	#this method will run every time a document is saved
    def before_save(self):
        self.full_name = f'{self.first_name} {self.last_name or ""}'
        frappe.msgprint(f"Saving Book")
        # data =  frappe.get_all('Article', fields=['article'])
        # print(data)

    # def validate(self):
    #     if not self.author:
    #         frappe.throw("Author is required")

    # def after_insert(self):
    #     frappe.msgprint(f"Book {self.title} has been added successfully!")
