// Copyright (c) 2025, codeWithSwapnil and contributors
// For license information, please see license.txt

frappe.ui.form.on("server side script", {
	first_name:function(frm){
		frm.call({
			doc:frm.doc,
			method:'frm_call',
			arg:{
				msg:"hello"
			},
			freeze:true, //ye freeze karega screen ko jab tak method call nahi hogi tab tak
			freeze_message:__("calling frm_call method..."), //this is  freeze message show user while method is running
			callback:function(r){
				// frappe.msgprint(r.message)
			}
		})
	}

});
