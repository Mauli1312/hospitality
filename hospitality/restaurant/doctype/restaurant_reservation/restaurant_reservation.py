# Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from datetime import timedelta
from frappe.model.document import Document
from frappe.utils import get_datetime

class RestaurantReservation(Document):
    def validate(self):
        # Set default value for reservation_end_time if not provided
        if not self.reservation_end_time:
            self.set_default_end_time()

    def set_default_end_time(self):
        # Calculate end time as one hour after the reservation_time
        self.reservation_end_time = get_datetime(self.reservation_time) + timedelta(hours=1)
