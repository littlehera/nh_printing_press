// Copyright (c) 2016, creamdory and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["75-74-72"] = {
	"filters": [
        {
            "fieldname": "work_docket",
            "label": __("Work Docket No"),
            "fieldtype": "Link",
			"options": "Sales Order",
            "reqd": 1,
            // "get_options": function() {
            //
            // }
        },
	]
}
