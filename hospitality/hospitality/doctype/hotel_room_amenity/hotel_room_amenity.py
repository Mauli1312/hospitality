# Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from frappe.model.document import Document
import frappe

class HotelRoomAmenity(Document):
    # New fields
    def validate(self):
        # Example validation: Ensure that the quantity is positive
        if self.quantity <= 0:
            frappe.throw("Quantity must be a positive number.")

    # Custom method to calculate total cost
    def calculate_total_cost(self):
        self.total_cost = self.rate * self.quantity
