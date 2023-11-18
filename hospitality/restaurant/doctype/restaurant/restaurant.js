// Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Restaurant', {
	refresh: function(frm) {
		// Add a custom button to create a new Order Entry
		frm.add_custom_button(__('Create Order'), () => {
			createNewOrder();
		});
	},
});

// Function to handle the creation of a new Order Entry
function createNewOrder() {
	frappe.model.open_mapped_doc({
		method: 'create_new_order_entry',
		frm: cur_frm,
	});
}
