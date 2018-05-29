// Copyright (c) 2016, creamdory and contributors
// For license information, please see license.txt

var d = new Date();
frappe.query_reports["Job Done File"] = {

	"filters": [
	    {
            "fieldname": "from_date",
            "label": __("Date Start"),
            "fieldtype": "Date",
            "reqd": 1,
            "default": new Date(d.getFullYear(),d.getMonth(),1),
        },
        {
            "fieldname": "to_date",
            "label": __("Date End"),
            "fieldtype": "Date",
            "reqd": 1,
            "default": new Date(d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate()),
        },
        // {
        //     "fieldname": "work_docket",
        //     "label": __("Work Docket No"),
        //     "fieldtype": "Link",
			// "options": "Sales Order",
        //     // "reqd": 1
        // },

	]
}
