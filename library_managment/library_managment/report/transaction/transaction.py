# Copyright (c) 2025, codeWithSwapnil and contributors
# For license information, please see license.txt

# import frappe


import frappe
from frappe.utils.data import formatdate

def execute(filters=None):
    columns = [
        {"fieldname": "article", "label": "Article", "fieldtype": "Data", "width": 200},
        {"fieldname": "type", "label": "Type", "fieldtype": "Data", "width": 100},
        {"fieldname": "library_member", "label": "Library Member", "fieldtype": "Data", "width": 150},
        {"fieldname": "date", "label": "Date", "fieldtype": "Date", "width": 120}
    ]

    # SQL query to fetch transaction data
    data = frappe.db.sql("""
        SELECT article, type, library_member, date
        FROM `tabLibrary Transaction`
        ORDER BY date DESC
    """, as_dict=True)

    # Format date nicely
    for d in data:
        d['date'] = formatdate(d['date'])

    # Chart data: number of transactions by type
    type_count = frappe.db.sql("""
        SELECT type, COUNT(name) as total
        FROM `tabLibrary Transaction`
        GROUP BY type
    """, as_dict=True)

    chart = {
        "data": {
            "labels": [d.type for d in type_count],
            "datasets": [{"name": "Transactions", "values": [d.total for d in type_count]}]
        },
        "type": "bar",
        "height": 300
    }

    return columns, data, None, chart
