// Copyright (c) 2025, codeWithSwapnil and contributors
// For license information, please see license.txt

frappe.query_reports["report for article"] = {
	"filters": [

			{
			"fieldname":"author",
			"fieldtype": "Data",
			"label": "author"
			},
			{
			"fieldname":"article",
			"fieldtype": "Link",
			"label": "articles",
			"options":"Article"
			},
			// {
			// 	"fieldname":"from_date",
			// 	"fieldtype":"Date",
			// 	"label":"from date",
			// 	"default":dateutil.year_start()
			// }

	],
	//  "onload": function (report) {
	// 	// Chart create karne ke liye initial config
	// 	report.page.add_inner_button(__('Show Chart'), function () {
	// 		let data = report.data;

	// 		// Count of articles by author
	// 		let chart_data = {};
	// 		data.forEach(d => {
	// 			if (chart_data[d.author]) {
	// 				chart_data[d.author] += 1;
	// 			} else {
	// 				chart_data[d.author] = 1;
	// 			}
	// 		});

	// 		const labels = Object.keys(chart_data);
	// 		const values = Object.values(chart_data);

	// 		frappe.show_chart({
	// 			data: {
	// 				labels: labels,
	// 				datasets: [
	// 					{
	// 						name: "Articles Count",
	// 						values: values
	// 					}
	// 				]
	// 			},
	// 			type: 'pie',  // 'bar' for bar chart
	// 			title: 'Articles by Author'
	// 		});
	// 	});
	// }
};
