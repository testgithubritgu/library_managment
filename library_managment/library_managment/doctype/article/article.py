# Copyright (c) 2025, codeWithSwapnil and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class Article(WebsiteGenerator):
	pass


@frappe.whitelist()
def get_all_article_records():
    articles = frappe.get_all(
        "Article",
        fields = ["article"]
	)
    return articles

@frappe.whitelist()
def change_status_articles(article):
    try:
        # Allow only POST requests
        if frappe.request.method != "POST":
            frappe.throw("Invalid request method. It should be POST.")

        # Fetch the Article document
        articles = frappe.get_doc("Article", article)

        # Update the status
        articles.status = "Issued"
        articles.save()

        # Return confirmation response
        return {"status": articles.status, "name": articles.name}

    except Exception as e:
        frappe.log_error(title="Change Status Error", message=frappe.get_traceback())
        return {"error": str(e)}

