# Copyright (c) 2025, Saranesh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Transaction(Document):
	pass


@frappe.whitelist()
def calculate_in_hand_money():
    transactions = frappe.get_all("Transaction", ["transaction_type", "amount", "name"])
    
    income = expense = investment = 0
    for transaction in transactions:
        income += transaction.amount if transaction.transaction_type == "Income" else 0
        expense += transaction.amount if transaction.transaction_type == "Expense" else 0
        investment += transaction.amount if transaction.transaction_type == "Investment" else 0
        
    in_hand = income - (expense + investment)
    
    return {"value": in_hand, "currency": "INR"}