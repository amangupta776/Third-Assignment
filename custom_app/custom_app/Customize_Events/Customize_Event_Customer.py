import frappe
import frappe.utils

def validateDate(doc,method):
    # This Function Check Customer Anniversary Date is Not more than today Date
    if doc.custom_customer_anniversary and doc.custom_customer_anniversary > frappe.utils.today():
        frappe.throw("You Can't Choose Future Date")
 

def customFunc(a,b):
    print("Before breakpoint")
    import ipdb; ipdb.set_trace()  
    result = a + b
    print(f"Result: {result}")
    return result

def customError():
    try:
        a=1/0
        print(a)
    except Exception as e:
        frappe.log_error("Can't Divided By 0")