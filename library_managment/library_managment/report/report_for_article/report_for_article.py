import frappe

# def execute(filters=None):
    # frappe.msgprint(str(filters))
    # if not filters:
    #     filters = {}

    # # Columns define kar
    # columns = [
    #     {"label": "Article Name", "fieldname": "article", "fieldtype": "Data", "width": 200},
    #     {"label": "Author", "fieldname": "author", "fieldtype": "Data", "width": 150},
    #     {"label": "Publisher", "fieldname": "publisher", "fieldtype": "Data", "width": 120},
    #     {"label": "status", "fieldname": "status", "fieldtype": "Data", "width": 120},
    # ]

    # # Filter ke hisaab se conditions banao
    # conditions = []

    # if filters.get("author"):
    #     conditions.append("LOWER(author) LIKE LOWER(%(author)s)")
    #     filters["author"] = f"%{filters['author']}%"

    # if filters.get("article"):
    #     conditions.append("LOWER(article) LIKE LOWER(%(article)s)")
    #     filters["article"] = f"%{filters['article']}%"

    # condition_str = ""
    # if conditions:
    #     condition_str = "WHERE " + " AND ".join(conditions)

    # # SQL query likh
    # query = f"""
    #     SELECT
    #         article,
    #         author,
    #         publisher
    #     FROM `tabArticle`
    #     {condition_str}
    #     ORDER BY modified DESC
    # """

    # data = frappe.db.sql(query, filters, as_dict=True)

    # return columns, data


# import frappe

def execute(filters=None):
    columns = [
        {"fieldname": "article", "label": "Article", "fieldtype": "Data"},
        {"fieldname": "author", "label": "Author", "fieldtype": "Data"},
        {"fieldname": "publisher", "label": "Publisher", "fieldtype": "Data"}
    ]

    data = frappe.db.sql("""
        SELECT
            article,
            author,
            publisher
        FROM `tabArticle`
        ORDER BY modified DESC
    """, as_dict=True)

    # Chart data
    chart = {
        "data": {
            "labels": [d.article for d in data],
            "datasets": [
                {
                    "name": "Articles Count",
                    "values": [1 for d in data]   # simple value for each article
                }
            ]
        },
        "type": "bar",   # can be 'line', 'bar', 'pie'
        "height": 300
    }

    return columns, data, None, chart
