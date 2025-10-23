// Copyright (c) 2025, codeWithSwapnil and contributors
// For license information, please see license.txt

frappe.query_reports["transaction"] = {
	onload: function (report) {
		// Example: add filter
		report.page.add_field({
			fieldname: "library_member",
			label: "Library Member",
			fieldtype: "Link",
			options: "Library Member",
			change: function () {
				report.refresh();
			}
		});
	},
	formatter: function (value, row, column, data, default_formatter) {
		value = default_formatter(value, row, column, data);
		if (column.fieldname === "type") {
			if (data.type === "Issue") {
				value = `<span style="color: red; font-weight: bold;">${value}</span>`;
			} else {
				value = `<span style="color: green; font-weight: bold;">${value}</span>`;
			}
		}
		return value;
	}
};
