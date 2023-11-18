# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.utils import add_days, date_diff
from hospitality.hotels.doctype.hotel_room_reservation.hotel_room_reservation import get_rooms_booked

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data

def get_columns():
    columns = [
        dict(label=_("Room Type"), fieldname="room_type"),
        dict(label=_("Rooms Booked"), fieldtype="Int")
    ]
    return columns

def get_data(filters):
    out = []
    room_types = frappe.get_all('Hotel Room Type')

    for room_type in room_types:
        total_booked = calculate_total_booked(room_type.name, filters.from_date, filters.to_date)
        out.append([room_type.name, total_booked])

    return out 

def calculate_total_booked(room_type, from_date, to_date):
    total_booked = 0
    for i in range(date_diff(to_date, from_date)):
        day = add_days(from_date, i)
        total_booked += get_rooms_booked(room_type, day)

    return total_booked
