// Copyright (c) 2016, creamdory and contributors
// For license information, please see license.txt

frappe.query_reports["Plate Room"] = {
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
