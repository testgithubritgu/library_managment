// Copyright (c) 2025, codeWithSwapnil and contributors
// For license information, please see license.txt

async function fetchBookDetails(book_name) {
	let r = await frappe.call({
		method: "library_managment.library_managment.api.api.py.get_book_details",
		args: { book_name }
	});
	frappe.msgprint("Author: " + r.message.author);
}
