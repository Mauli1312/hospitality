# Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and Contributors
# See license.txt

import unittest
import frappe

from hospitality.hospitality.doctype.hotel_room_reservation.hotel_room_reservation import (
    HotelRoomPricingNotSetError,
    HotelRoomUnavailableError,
)

test_dependencies = ["Hotel Room Package", "Hotel Room Pricing", "Hotel Room"]


class TestHotelRoomReservation(unittest.TestCase):
    def setUp(self):
        self.cleanup_reservations()

    def tearDown(self):
        self.cleanup_reservations()

    def cleanup_reservations(self):
        reservations = frappe.get_all("Hotel Room Reservation", filters={}, fields=["name"])
        for reservation in reservations:
            frappe.delete_doc("Hotel Room Reservation", reservation.name)

    def test_reservation(self):
        reservation = make_reservation(
            from_date="2017-01-01",
            to_date="2017-01-03",
            items=[
                dict(item="Basic Room with Dinner", qty=2)
            ]
        )
        reservation.insert()
        self.assertEqual(reservation.net_total, 48000, "Net total calculation is incorrect")

    def test_price_not_set(self):
        reservation = make_reservation(
            from_date="2016-01-01",
            to_date="2016-01-03",
            items=[
                dict(item="Basic Room with Dinner", qty=2)
            ]
        )
        with self.assertRaises(HotelRoomPricingNotSetError):
            reservation.insert()

    def test_room_unavailable(self):
        make_reservation(
            from_date="2017-01-01",
            to_date="2017-01-03",
            items=[
                dict(item="Basic Room with Dinner", qty=2),
            ]
        ).insert()

        reservation = make_reservation(
            from_date="2017-01-01",
            to_date="2017-01-03",
            items=[
                dict(item="Basic Room with Dinner", qty=20),
            ]
        )
        with self.assertRaises(HotelRoomUnavailableError):
            reservation.insert()


def make_reservation(**kwargs):
    kwargs["doctype"] = "Hotel Room Reservation"
    if "guest_name" not in kwargs:
        kwargs["guest_name"] = "Test Guest"
    doc = frappe.get_doc(kwargs)
    return doc
