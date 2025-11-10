# Copyright (c) 2025, Saranesh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import timedelta
from frappe.utils import getdate


class FinanceTransaction(Document):
	def before_save(self):
		if not self.transactions or self.has_value_changed("posting_date"):
			self.set("weekly_dates", [])
			amount = self.amount_to_be_collected / 12
			for i in range(1, 13):
				next_date = getdate(self.posting_date) + timedelta(weeks=i)
				self.append("transactions", {
					"actual_date": next_date,
					"amount": amount
					}
				)
				
		self.total_paid_amount = 0
		for transaction in self.transactions:
			if transaction.paid_date: 
				self.total_paid_amount += transaction.amount
			 
		self.outstanding = self.amount_to_be_collected - self.total_paid_amount