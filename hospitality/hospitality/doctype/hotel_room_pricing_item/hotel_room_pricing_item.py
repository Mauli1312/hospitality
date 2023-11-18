# Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from frappe.model.document import Document

class HotelRoomPricingItem(Document):
    def validate(self):
        # Example validation: Ensure that the rate is greater than 0
        if self.rate <= 0:
            frappe.throw("Rate must be greater than 0.")

    def calculate_total_cost(self):
        # Example custom method: Calculate total cost
        if self.quantity and self.rate:
            total_cost = self.quantity * self.rate
            self.total_cost = total_cost
