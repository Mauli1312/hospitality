# Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and Contributors
# See license.txt

import unittest
from frappe.utils import getdate
from frappe.utils import add_days
from frappe.utils import add_months
from frappe.utils import add_years
from frappe.utils import get_last_day

class TestHotelRoomPricingPackage(unittest.TestCase):
    def test_valid_total_price(self):
        # Add your test logic here
        pricing_package = frappe.get_doc("Hotel Room Pricing Package", "Your Package Name")
        self.assertTrue(pricing_package.is_valid_total_price())

    def test_invalid_total_price(self):
        # Add another test case
        pricing_package = frappe.get_doc("Hotel Room Pricing Package", "Your Package Name")
        pricing_package.total_price = -500  # An invalid total price
        self.assertFalse(pricing_package.is_valid_total_price())

    def test_calculate_discounted_price(self):
        # Add another test case
        pricing_package = frappe.get_doc("Hotel Room Pricing Package", "Your Package Name")
        discounted_price = pricing_package.calculate_discounted_price()
        self.assertEqual(discounted_price, expected_discounted_price)
