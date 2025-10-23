// Copyright (c) 2025, codeWithSwapnil and contributors
// For license information, please see license.txt

frappe.ui.form.on("client side scripting", {

	first_name:function(frm){
		frappe.call({
			method:"library_managment.library_managment.doctype.server_side_script.server_side_script.frm_call",
			args:{
				msg:"swapnil sir"
			},
			freeze:true,
			freeze_message:__("this is freezmsg"),
			callback:function(r){
				frappe.msgprint(r.message)
			}
		})
	}
	// refresh(frm) {
	// 	frappe.msgprint("HEY bhai User!!!")
	// },

	/////////////////////////////////////////////////////////////////////////////////////
	///------------------------->>>>>>>>set_intro() & frm.is_new()<<<<<</////////////////
	/////////////////////////////////////////////////////////////////////////////////////

	//----------------- THIS FUNCTION BASICALLY WORK ON SET INRTO LIKE WHEN USER OPEN NEW FORM --------
	// refresh:function(frm){
	// 	if(frm.is_new()){
	// 		frm.set_intro("create one record")
	// 	}
	// }






	/////////------------->>>>>>>>>>>>>>>>>>AFTER SAVE ye CHAlega <<<<<<<<<<<----------------
	// after_save: function (frm) {
	// 	if (frm.doc.family_members && frm.doc.family_members.length > 0) {
	// 		for (let row of frm.doc.family_members) {
	// 			frappe.msgprint(__(`The full name is ${row.name1} (${row.relation})`));
	// 		}
	// 	}
	// }

	//////////////////------------------------Ye Line use feild ko mandatory karegi condition ke base pe ------------
	// first_name:function(frm){
	// 	frm.set_df_property("email","reqd",1)
	// }

	// ------------------------------------->>>> AFTER SAVE <<<<-------------------------------------
	// after_save:function(frm){
	// 	// frappe.msgprint(`the full name of the person is ${frm.doc.first_name} ${frm.doc.last_name}`)
	// }



	//---------------------------------->>>>>> This will Set the value in that selected field <<<<<<------------------------
	// validate:function(frm){
	// 	frm.set_value("full_name",frm.doc.first_name + " " + frm.doc.last_name)
	// }

	// ------------------------------------->>>>>>>> Add Childe <<<<<<<<-------------------------------
	// validate:function(frm){
	// 	let row = frm.add_child("family_members",{
	// 		name:"john doe",
	// 		relation:"father",
	// 		age:26
	// 	})
	// }

	// -------------------->>>>>>>>>>>>>>>>> make any field as mandotory using  enable <<<<<<<<<<<<<<------------------
	// enable:function(frm){
	// 	//........THis will make that field is required..........
	// 	frm.set_df_property("first_name","reqd",1)

	// 	//........This will make that make last_name field as read onlye...............
	// 	frm.set_df_property("last_name","read_only",1)
	// }


	//--------------------------------This fuction add client side scripting adding buttons in dropdown ---------------
	// refresh:function(frm){
// 		frm.add_custom_button("click me",()=>{
// 			frappe.db.get_value("Article",{"article":"spiderman"},"article").then(r =>{

// 				// __ <<< ye line kya krti hai Agar tu English ke alawa koi aur language (for example Hindi, French, Arabic, etc.) enable kare system me,
// // to __() ke andar ka text automatic us language me translate ho sakta hai — provided translation available ho.
// 				if (r && r.message){
// 					frappe.msgprint(__("Article : " + r.message.article))

// 				}else{
// 					frappe.msgprint(__("no record found"))
// 				}
// 			})
// 		},"button Drop")
// 		frm.add_custom_button("click me",()=>{
// 			frappe.db.get_value("Article",{"article":"spiderman"},"article").then(r =>{

// 				// __ <<< ye line kya krti hai Agar tu English ke alawa koi aur language (for example Hindi, French, Arabic, etc.) enable kare system me,
// // to __() ke andar ka text automatic us language me translate ho sakta hai — provided translation available ho.
// 				if (r && r.message){
// 					frappe.msgprint(__("Article : " + r.message.article))

// 				}else{
// 					frappe.msgprint(__("no record found"))
// 				}
// 			})
// 		},"button Drop")
	// }


	//////////////////////////////////////////////////////////////////
	////////////////////////BEFORE CANCELE & after cancel////////////////////////////
	/////////////////////////////////////////////////////////////////
	// before_cancel:function(frm){
	// 	frappe.throw(`bhai cancel nahi kar sakte bahi`)
	// }

	// after_cancel:function(frm){
	// 	frappe.throw('cancel ')
	// }




});









/////////////////////////////////////////////////////////////////////////////////////////////
//------------------->>>>> ADDING EVENTS ON CHILD FIELD CHANGES <<<<<<<----------------------
//////////////////////////////////////////////////////////////////////////////////////////////

frappe.ui.form.on("Family Members", {
// 	name1: function (frm, cdt, cdn) {
// 		frappe.msgprint("Child row ka name field trigger hua!");
// 	}
});
