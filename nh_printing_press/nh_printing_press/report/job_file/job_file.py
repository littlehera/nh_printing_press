# Copyright (c) 2013, creamdory and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
    columns = [
        _("Work Docket No") + ":Link/Sales Order:125",
        _("Transaction Date") + ":Date:125",
        _("Customer Name") + ":Link/Customer:200",
        _("Quote No") + "::100",
        _("LPO No") + "::100",
        _("Invoice No") + "::100",
        _("Flow Status") + "::150",
        _("Received By") + "::170",
    ]
    data = []
    from_date = filters.get("from_date")
    to_date = filters.get("to_date")

    wd = frappe.db.sql("""Select transaction_date, name, customer_name, quote_no, lpo_no, flow_status, received_by, invoice_no
					  from `tabSales Order` where docstatus != 2 and transaction_date >= %s
					  and transaction_date <= %s and flow_status != 'Job Done'""", (from_date, to_date))

    for w in wd:
        date = w[0]
        name = w[1]
        customer_name = w[2]
        quote_no = w[3]
        lpo_no = w[4]
        flow_status = w[5]
        received_by = w[6]
        inv_no = w[7]

        data.append([name, date, customer_name, quote_no, lpo_no, inv_no, flow_status,received_by])

    return columns, data
