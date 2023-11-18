# Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from frappe.model.document import Document

class HotelRoomPricing(Document):
    def validate(self):
        # Example validation: Ensure that the pricing is greater than 0
        if self.price <= 0:
            frappe.throw("Price must be greater than 0.")

    def calculate_discounted_price(self):
        # Example custom method: Calculate discounted price
        if self.discount_percentage:
            discounted_price = self.price - (self.price * (self.discount_percentage / 100))
            self.discounted_price = discounted_price
