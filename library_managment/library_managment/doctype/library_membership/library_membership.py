# Copyright (c) 2025, codeWithSwapnil and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus

class LibraryMembership(Document):


    def before_submit(self):
        # Check if there is already a submitted membership for this member
        # that ends after this membership's start date
        exists = frappe.db.exists(
            "Library Membership",
            {
                "library_member": self.library_member,
                "docstatus": DocStatus.submitted(),
                "to_date": (">", self.from_date),
            },
        )

        if exists:
            frappe.throw("There is an active membership for this member.")
        loan_period = frappe.db.get_single_value("Library Setting", "loan_period")
        self.to_date = frappe.utils.add_days(self.from_date, loan_period or 30)
