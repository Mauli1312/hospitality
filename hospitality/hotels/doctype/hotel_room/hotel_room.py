# Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class HotelRoom(Document):
    def validate(self):
        """
        Validate and set default values for capacity and extra bed capacity based on Hotel Room Type.
        """
        if not self.capacity:
            # Fetch values from Hotel Room Type and set defaults
            room_type_doc = frappe.get_doc('Hotel Room Type', self.hotel_room_type)
            
            if room_type_doc:
                self.capacity = room_type_doc.capacity
                self.extra_bed_capacity = room_type_doc.extra_bed_capacity
            else:
                frappe.throw("Hotel Room Type not found: {}".format(self.hotel_room_type))
