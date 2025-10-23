import frappe

def get_context(context):
	# do your magic here
	pass

@frappe.whitelist()
def getFrappeDetails():
	return "swaptech"
