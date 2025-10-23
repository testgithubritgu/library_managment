# Copyright (c) 2025, codeWithSwapnil and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class serversidescript(Document):
	# def validate(self):
	# 	frappe.msgprint("helo welcome to our world")
	# def before_insert(self):
	# 	frappe.throw("error for inserting doc")
	# def before_save(self):
	# 	frappe.throw('err')
	# def on_update(self):
	# 	frappe.throw("yes bro on update")
    # def before_submit(self):
    #     frappe.throw("this is before submite event")
	# def on_cancel(self):
	# 	frappe.msgprint("this is on cancel event trigger")
    # def on_trash(self):
    #     frappe.msgprint("bhai delet ho gaya")
    # def after_delete(self):
    #     frappe.msgprint("this is after deletion message")



	# /////////////////////////////////////////////////////////////////////////////////////////
    # /////////////////////////////backend data fetching///////////////////////////////////////
	# /////////////////////////////////////////////////////////////////////////////////////////

	# def validate(self):
	# 	self.get_value()

	# def get_value(self):
	# 	# Set the value in the database
	# 	frappe.db.set_value("client side scripting", "swapnil", "age", 34)

	# 	# Fetch multiple values
	# 	first_name, age = frappe.db.get_value("client side scripting", "swapnil", ["first_name", "age"])

	# 	# Show a message to the user
	# 	frappe.msgprint(f"The message is {first_name} and {age}")


	# ---------------------------->>>>>>>>>>>>>>>>THIS FUNCTION IS CHECKS WHETHER THE document IS exists OR NOT <<<--------------

	# def validate(self):
	# 	if frappe.db.exists("client side scripting", "swapnil"):
	# 		frappe.msgprint("Document exists!")
	# 	else:
	# 		frappe.msgprint("Document does not exist.")


	# ---------------------------------Return the count of number of document exists in doctype ==================
    # def validate(self):
    #     data =  frappe.db.count("client side scripting",{"last_name":"s"})
    #     frappe.msgprint(f"total number of data present on doctype {data}")



	# ------------------------------------this is sql query----------------------------------
	# def validate(self):
	# 	self.sql()

	# def sql(self):
	# 	data = frappe.db.sql("""
	# 							SELECT first_name ,last_name
	# 				 		    FROM `tabclient side scripting`
	# 				   			WHERE first_name = 'swapnil'

	# 						""",as_dict = 1)
	# 	for d in data:
	# 		frappe.msgprint(f"hey this is from client side scripting {d.first_name} and last_name is  {d.last_name}")



	#..................................... fetch values ........................................
    # def validate(self):
    #     data  = frappe.get_doc("Article",self.first_name)
    #     frappe.msgprint(f"this client side scripting {data.author} {data.publisher}")
    # def validate(self):
	# 	  # yahan self.doc nahi likhna, sirf self.flags check karo
	# 	if not getattr(self.flags,"from_server",False):
	# 		self.newDocument()
	# def newDocument(self):
	# 	doc = frappe.new_doc("client side scripting")
	# 	doc.first_name = "swapnil bhaiaee"
	# 	doc.last_name = "raut"
	# 	doc.age = 45
	# 	doc.flags.from_server = True # flag set to prevent recursion
	# 	doc.append("family_members",{
	# 		"name1":"d1",
	# 		"relation":"father",
	# 		"age":33
	# 	})
	# 	doc.insert()

	# ///////////////////////////////////DELETe DOC /////////////////////////////////////////
    # def validate(self):
    #     frappe.delete_doc("client side scripting","swapnil")



	# //////////////////////////////////////// SAVE THE RECORD /////////////////////////////////////
    # ///////////////////////////////////////////////////////////////////////////////////////////////

	# def validate(self):
	# 	self.addNewDoc()
	# def addNewDoc(self):
	# 	doc = frappe.new_doc("client side scripting")
	# 	doc.first_name = "swapnilsir"
	# 	doc.age = 25
	# 	#ignore write permition during insert
	# 	#-User ke write permission check ko bypass karta hai. Useful jab system ya server-side code se doc create kar rahe ho.



	# 	#  # do not create a version record
	# 	# Normally Frappe har update pe “Version” record banata hai (change history ke liye). Isse True karne se wo skip hota hai.
	# 	doc.save(ignore_permissions = True,
	# 		ignore_version = True
	# 	)

	# ////////////////////////////DELETE THE RECORD/////////////////////////////////////////
    # ///////////////////////////////////////////////////////////////////////////////////////
	# def validate(self):
	# 	self.db_set_doc()

	# def db_set_doc(self):
	# 	doc = frappe.get_doc("client side scripting","s")
	# 	doc.db_set("age",44)


	# //////////////////////////////////////////////////GET LIST FROM FRAPPE DB///////////////////////////////
	# //////////////////////////////////////////////////////////////////////////////////////////////////////////

	# def validate(self):
	# 	self.getList()
	# def getList(self):
	# 	doc = frappe.db.get_list("client side scripting",filters={"age":44},fields=["first_name","age"])
	# 	for d in doc:
	# 		frappe.msgprint(f"these are the list of matching name {d.first_name} {d.age}")

	# # ///////////////////////////////////////////////SERVER SIDE CALLS////////////////////////////////////
    # @frappe.whitelist()
    # def frm_call(self,msg):
    #     import time
    #     time.sleep(5)
    #     frappe.msgprint(msg)

	pass


        # return "this is from frm call method"


@frappe.whitelist()
def frm_call(msg):
	return f"hey boy {msg}"

