# Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import re
from frappe.model.document import Document
from frappe.model.naming import make_autoname

class RestaurantTable(Document):
    def autoname(self):
        # Replace spaces with hyphens and ensure single hyphen between words
        prefix = re.sub(r'\s+', '-', self.restaurant)
        
        # Generate an autoname using the formatted prefix
        self.name = make_autoname(f'{prefix}-.##')
