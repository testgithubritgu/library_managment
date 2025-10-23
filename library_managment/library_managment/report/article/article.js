// Copyright (c) 2025, codeWithSwapnil and contributors
// For license information, please see license.txt

frappe.query_reports["Article"] = {
	"filters": [
		{
			"fieldname":"name",
			"label":__("article"),
			"fieldtype":"Link",
			"options":"Article"
		},
		{
			"fieldname":"dob",
			"label":__("DOB"),
			"fieldtype":"Date"

		},
		{"fieldname":"age",
			"label":"age",
			"fieldtype":"Data"
		}
	]
};
