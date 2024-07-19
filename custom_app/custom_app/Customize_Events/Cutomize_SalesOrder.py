import frappe

# This Function Send Mail When Sales Order Is Approved
def send_email_on_approval(doc, method):
    if doc.workflow_state == 'Approved':
        recipients = ["amanhyper41@gmail.com"]  
        subject = f'Sales Order {doc.name} Approved'
        message = f'''
        Dear Aman,

        Your Sales Order {doc.name} has been approved.
        
        '''
        
        frappe.sendmail(
            recipients=recipients,
            subject=subject,
            message=message,
            delayed=False
        )

