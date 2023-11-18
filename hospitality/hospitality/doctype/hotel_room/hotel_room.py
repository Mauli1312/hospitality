# Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class HotelRoom(Document):
    def validate(self):
        if not self.capacity:
            room_type = frappe.get_doc('Hotel Room Type', self.hotel_room_type)
            self.capacity = room_type.capacity if room_type else None
            self.extra_bed_capacity = room_type.extra_bed_capacity if room_type else None
