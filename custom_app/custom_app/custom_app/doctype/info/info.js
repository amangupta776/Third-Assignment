// Copyright (c) 2024, Aman and contributors
// For license information, please see license.txt

frappe.ui.form.on("Info", {
	refresh(frm) {

       frm.add_custom_button("dailog box",()=>{
        let dilogbox = new frappe.ui.Dialog({
            title: 'Dailog Box',
            fields: [
                {
                    label: 'Name',
                    fieldname: 'name1',
                    fieldtype: 'Data'
                },{
                    label:'Age',
                    fieldname:"age",
                    fieldtype:'Data'
                }
            ],
            primary_action_label: 'submit',
            primary_action(values) {
               frm.doc.name1=values.name1
                    frm.doc.age=values.age
               frm.save()
               
                dilogbox.hide();  
            }
        });
        dilogbox.show();

      })
	},
});
