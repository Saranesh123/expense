// Copyright (c) 2025, Saranesh and contributors
// For license information, please see license.txt

frappe.ui.form.on("Finance Transaction", {
	actual_amount(frm) {
        if (frm.doc.actual_amount && frm.doc.amount_to_be_collected) {
            frm.set_value("difference", frm.doc.amount_to_be_collected - frm.doc.actual_amount);
        }
	},

    amount_to_be_collected(frm) {
        frm.trigger("actual_amount");
    }
});
