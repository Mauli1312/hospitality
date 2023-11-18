# Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class RestaurantMenu(Document):
    def validate(self):
        # Set default rate for items if not provided
        for item in self.items:
            if not item.rate:
                item.rate = frappe.db.get_value('Item', item.item, 'standard_rate')

    def on_update(self):
        # Sync Price List on update
        self.make_price_list()

    def on_trash(self):
        # Clear prices on trash
        self.clear_item_price()

    def clear_item_price(self, price_list=None):
        # Clear all item prices for this menu
        if not price_list:
            price_list = self.get_price_list().name
        frappe.delete_doc('Item Price', {'price_list': price_list})

    def make_price_list(self):
        # Create or update price list for the menu
        price_list = self.get_price_list()
        self.db_set('price_list', price_list.name)

        # Delete old items
        self.clear_item_price(price_list.name)

        # Insert new items
        for item in self.items:
            frappe.get_doc({
                'doctype': 'Item Price',
                'price_list': price_list.name,
                'item_code': item.item,
                'price_list_rate': item.rate
            }).insert()

    def get_price_list(self):
        # Get or create price list for the menu
        price_list_name = frappe.db.get_value('Price List', {'restaurant_menu': self.name})
        
        if price_list_name:
            price_list = frappe.get_doc('Price List', price_list_name)
        else:
            price_list = frappe.new_doc('Price List')
            price_list.restaurant_menu = self.name
            price_list.price_list_name = self.name

        price_list.enabled = 1
        price_list.selling = 1
        price_list.save()

        return price_list
