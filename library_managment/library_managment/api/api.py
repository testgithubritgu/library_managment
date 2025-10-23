import frappe

@frappe.whitelist()   # 👈 makes it accessible from JS
def get_book_details(book_name):
    try:
        book = frappe.get_doc("Article", book_name)
        return {
            "title": book.article,    # or book.article if that is your field
            "author": book.author
        }
    except Exception as e:
        return {"msg": str(e)}
@frappe.whitelist()
def create_post(article, author, publisher,status):
    """
    API method to create a new Post (DocType: Post)
    """
    # DocType: Post (example) me data insert karna
    doc = frappe.get_doc({
        "doctype": "Article",
        "article": article,
        "author": author,
        "publisher": publisher,
        "status":status,
    })
    doc.insert()
    frappe.db.commit()  # commit changes
    return {"status": "success", "post_name": doc.name}

@frappe.whitelist()
def del_record_article_doctype(doctype,name):
    """
    API method to delete a record by name
    """
    try:
        # Delete the record
        frappe.delete_doc(doctype, name)
        frappe.db.commit()
        return {"status": "success", "message": f"{doctype} {name} deleted successfully"}

    except frappe.DoesNotExistError:
        return {"status": "error", "message": f"{doctype} {name} does not exist"}

    except Exception as e:
        return {"status": "error", "message": str(e)}

@frappe.whitelist()
def get_filtered_data(doctype, filters=None, fields=None, limit=100):
    """
    Generic method to fetch data from any Doctype using filters and selected fields.

    Args:
        doctype (str): Name of the Doctype
        filters (dict, optional): Filters to apply, e.g. {"status": "Issued"}
        fields (list, optional): Fields to fetch, e.g. ["name", "title", "status"]
        limit (int, optional): Number of records to fetch, default 100

    Returns:
        list of dict: List of matching records
    """
    try:
        # Ensure filters is a dict
        filters = filters or {}
        fields = fields or ["*"]  # Default all fields

        # Fetch data
        data = frappe.get_all(
            doctype,
            filters=filters,
            fields=fields,
            limit=limit
        )

        return {"data": data, "count": len(data)}

    except Exception as e:
        frappe.log_error(title="Get Filtered Data Error", message=frappe.get_traceback())
        return {"error": str(e)}
