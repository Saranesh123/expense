// Copyright (c) 2025, Saranesh and contributors
// For license information, please see license.txt

frappe.ui.form.on("Transaction", {
	setup(frm) {
        frm.set_query("category", () => {
            return {
                filters: {
                    transaction_type: frm.doc.transaction_type
                }
            }
        })
	},
});
