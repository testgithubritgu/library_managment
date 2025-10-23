frappe.ready(function() {
	// bind events here
	// if (frappe.web_form) {
	// 	frappe.web_form.on('after_load', () => {
	// 		frappe.msgprint('Welcome to Territory form');
	// 	});

	// let field = frappe.web_form.fields_dict.last_name;
	// if (field) {
	// 	field.$input.on('change', function () {
	// 		let val = $(this).val();
	// 		frappe.msgprint('Hi user, you entered: ' + val);
	// 	});
	// } else {
	// 	console.warn('Field last_name not found!');
	// }

	//--------------------------------------------->>> if last name is onchange event triggers <<<------------------------------
	// frappe.msgprint("hey swapnil")
	// frappe.timeout(0.2).then(() => {
	// 	// Access 'last_name' field safely
	// 	const last_name_field = frappe.web_form.fields_dict.last_name;
	// 	if (last_name_field && last_name_field.$input) {
	// 		// Bind change event
	// 		last_name_field.$input.on('change', function () {
	// 			const val = $(this).val();
	// 			frappe.msgprint("Hi user, you entered: " + val);
	// 		});
	// 	} else {
	// 		console.warn("last_name field not ready yet!");
	// 	}
	// })


	// frappe.web_form.after_load=()=>{
	// 	frappe.web_form.on("last_name",(field,value)=>{
	// 		frappe.msgprint("hi user")
	// 	})
	// }
	//---------------------------------------------->>>> age calculator age calculate on input date <<<---------------------------------
	// frappe.web_form.on('dob', (field, value) => {
	// 	if (value) {
	// 		dob = new Date(value);
	// 		var today = new Date();
	// 		var age = Math.floor(((today - dob) / (365.25 * 24 * 60 * 60 * 1000)));
	// 		frappe.web_form.set_value("age", [age])
	// 	}
	// });

	// ------------------------------------>>> email validations <<<---------------------------------------
	frappe.web_form.validate = ()=>{
		let email_id = frappe.web_form.get_value("primary_email");
		email_id = email_id.trim();

		var pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
		if(!pattern.test(email_id)&& email_id){
				frappe.msgprint("You entered email is not valid")
				return false;
		}

		//-------------------------------------- >>>>> Mobile  Validations <<<<< ----------------------------

		let mobilenum = frappe.web_form.get_value("cell_phone") || "";
		mobilenum = mobilenum.toString().trim()
		var validateMobNum = /^\+?\d{10,15}$/;
		let cleanedNumber = mobilenum.replace(/[\s-]/g, ""); // spaces aur hyphens remove

		//These are User  error Freindly Messages
		// if (!phon){
		// 	frappe.msgprint("pls Entet mobile number")
		// 	return false;
		// }
		// if (mobilenum.length !== 10){
		// 	frappe.msgprint("pls Enter valid Mobile Number")
		// 	return false
		// }


		if (mobilenum && !validateMobNum.test(cleanedNumber)){
			frappe.msgprint("Enter Valid Mobile Number")
			return false
		}
		return true

	}

	//-------------------------------------- >>>>> US Phone Validation <<<<< ----------------------------
	// let mobilenum = frappe.web_form.get_value("cell_phone") || "";
	// mobilenum = mobilenum.toString().trim(); // ensure string

	// // Remove any non-digit characters (like spaces, hyphens)
	// let digitsOnly = mobilenum.replace(/\D/g, "");

	// // Validate 10 digits exactly
	// if (digitsOnly.length !== 10) {
	// 	frappe.msgprint("Enter a valid 10-digit US phone number");
	// 	return false;
	// }


})
