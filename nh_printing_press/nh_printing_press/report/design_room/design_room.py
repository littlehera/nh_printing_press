# Copyright (c) 2013, creamdory and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe


def execute(filters=None):
    columns = [
        {"label": "Work Docket No", 'width': 200, "fieldname": "work_docket"},
        {"label": "Transaction Date", 'width': 200, "fieldname": "date"},
        {"label": "Customer Name", 'width': 205, "fieldname": "customer_name"},
        {"label": "Quote No", 'width': 135, "fieldname": "quote_no"},
        {"label": "LPO No", 'width': 135, "fieldname": "lpo_no"},
        # {"label": "Flow Status", 'width': 150, "fieldname": "flow_status"},
        # {"label": "Received By", 'width': 200, "fieldname": "received_by"},
    ]
    data = []

    work_docket = filters.get("work_docket")

    wd = frappe.db.sql("""Select transaction_date, name, customer_name, quote_no, lpo_no, flow_status, received_by
						  from `tabSales Order` where docstatus = 0 and name = %s""", (work_docket))

    for w in wd:
        date = w[0]
        name = w[1]
        customer_name = w[2]
        quote_no = w[3]
        lpo_no = w[4]
        flow_status = w[5]
        received_by = w[6]

        receive = "<button type ='submit' class='btn btn-primary btn-block' onclick = %s >Receive</button>" % (
            update_docket(name, frappe.session.user))
        # receive = "<button type ='button' onclick = %s >Receive</button>" % (
        # update_docket(name))

        data.append({"date": date, "work_docket": name,
                     "customer_name": customer_name,
                     "quote_no": quote_no,
                     "lpo_no": lpo_no,
                     # "flow_status": flow_status,
                     # "received_by": received_by,
                     })

    return columns, data


def update_docket(docket, user):
    frappe.db.sql("""Update `tabSales Order` set flow_status = 'Design Room', received_by = %s
	        where name = %s""", (user, docket))
    frappe.db.commit()
    print "Im Here++++++++"
    # frappe.msgprint("Successfully Received!")
    return frappe.msgprint("Successfully Received Docket " + docket + " in Design Room!")
