import frappe
import os
import barcode
from barcode.writer import ImageWriter


def on_save(doc, method):

    # create barcode for docname
    barcode_class = barcode.get_barcode_class('code39')
    ean = barcode_class(doc.name, ImageWriter(), add_checksum=False)
    barcode_path = frappe.get_site_path()+'/public/files/'
    ean.save(barcode_path+doc.name)
    save_image(barcode_path, doc.name)
    img_path = "/files/" + doc.name + ".png"
    doc.barcode_image = img_path
    doc.save()
    img_path = "/files/" + doc.name + ".png"
    frappe.db.sql("""Update `tabSales Order` set barcode_image = %s
                where name = %s""", (img_path, doc.name))
    frappe.db.commit()

def validate(doc, method):

    doc.received_by = frappe.session.user
    if not(doc.barcode_image):
        img_path = "/files/" + doc.name + ".png"
        frappe.db.sql("""Update `tabSales Order` set barcode_image = %s
                where name = %s""", (img_path, doc.name))
        frappe.db.commit()

def save_image(barcode_path,name):

    # save barcode image to file table
    attach_image = frappe.get_doc({
        "doctype": "File",
        "file_name": name,
        "file_url": barcode_path + name + '.png',
        "folder": 'Home/Attachments',
        "old_parent": 'Home/Attachments'
    })
    attach_image.insert()
