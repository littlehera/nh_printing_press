# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "nh_printing_press"
app_title = "NH Printing Press"
app_publisher = "creamdory"
app_description = "Printing Press"
app_icon = "octicon octicon-book"
app_color = "#2d701a"
app_email = "carrel@zambianlotto.co.zm"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/nh_printing_press/css/nh_printing_press.css"
# app_include_js = "/assets/nh_printing_press/js/nh_printing_press.js"

# include js, css files in header of web template
# web_include_css = "/assets/nh_printing_press/css/nh_printing_press.css"
# web_include_js = "/assets/nh_printing_press/js/nh_printing_press.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "nh_printing_press.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "nh_printing_press.install.before_install"
# after_install = "nh_printing_press.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "nh_printing_press.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
    # "*": {
    # 	"on_update": "method",
    # 	"on_cancel": "method",
    # 	"on_trash": "method"
    # },
    "Sales Order": {
        "after_insert": "nh_printing_press.wdevents.on_save",
        "validate": "nh_printing_press.wdevents.validate"
    },
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"nh_printing_press.tasks.all"
# 	],
# 	"daily": [
# 		"nh_printing_press.tasks.daily"
# 	],
# 	"hourly": [
# 		"nh_printing_press.tasks.hourly"
# 	],
# 	"weekly": [
# 		"nh_printing_press.tasks.weekly"
# 	]
# 	"monthly": [
# 		"nh_printing_press.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "nh_printing_press.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "nh_printing_press.event.get_events"
# }

fixtures = ["Custom Field", "Custom Script", "Property Setter", "Print Format", "Report", "Translation"]
