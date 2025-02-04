# Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from frappe import _

app_name = "hospitality"
app_title = "Hospitality"
app_publisher = "Frappe"
app_description = "Hospitality"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "pandikunta@frappe.io"
app_license = "MIT"

required_apps = ["erpnext"]

# Global Search Configuration
global_search_doctypes = {
    "Hospitality": [
        {'doctype': 'Hotel Room', 'index': 0},
        {'doctype': 'Hotel Room Reservation', 'index': 1},
        {'doctype': 'Hotel Room Pricing', 'index': 2},
        {'doctype': 'Hotel Room Package', 'index': 3},
        {'doctype': 'Hotel Room Type', 'index': 4}
    ]
}

# Domain Configuration
domains = {
    'Hospitality': 'hospitality.hospitality.hospitality',
}

# Includes in <head>
# ------------------
# Uncomment and set paths for custom JS and CSS files if needed
# app_include_css = "/assets/hospitality/css/hospitality.css"
# app_include_js = "/assets/hospitality/js/hospitality.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#    "Role": "home_page"
# }

# Generators
# ----------

# automatically create a page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to the Jinja environment
# jinja = {
#    "methods": "hospitality.utils.jinja_methods",
#    "filters": "hospitality.utils.jinja_filters"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#    "*": {
#        "on_update": "method",
#        "on_cancel": "method",
#        "on_trash": "method"
#    }
# }

# Scheduled Tasks
# ---------------
# Uncomment and set paths for custom scheduled tasks if needed
# scheduler_events = {
#    "all": [
#        "hospitality.tasks.all"
#    ],
#    "daily": [
#        "hospitality.tasks.daily"
#    ],
#    "hourly": [
#        "hospitality.tasks.hourly"
#    ],
#    "weekly": [
#        "hospitality.tasks.weekly"
#    ],
#    "monthly": [
#        "hospitality.tasks.monthly"
#    ],
# }

# Testing
# -------
# Uncomment and set paths for custom testing if needed
# before_tests = "hospitality.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#    "frappe.desk.doctype.event.event.get_events": "hospitality.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#    "Task": "hospitality.task.get_dashboard_data"
# }

# User Data Protection
# --------------------

# user_data_fields = [
#    {
#        "doctype": "{doctype_1}",
#        "filter_by": "{filter_by}",
#        "redact_fields": ["{field_1}", "{field_2}"],
#        "partial": 1,
#    },
#    {
#        "doctype": "{doctype_2}",
#        "filter_by": "{filter_by}",
#        "partial": 1,
#    },
#    {
#        "doctype": "{doctype_3}",
#        "strict": False,
#    },
#    {
#        "doctype": "{doctype_4}"
#    }
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#    "hospitality.auth.validate"
# ]

