frappe.ui.form.on('Custom Order Item', {
    qty: function(frm, cdt, cdn) {
        calculate_row_total(frm, cdt, cdn);
        calculate_total_cost(frm);
    },
    selling_price: function(frm, cdt, cdn) {
        calculate_row_total(frm, cdt, cdn);
        calculate_total_cost(frm);
    }
});

function calculate_row_total(frm, cdt, cdn) {
    let row = locals[cdt][cdn];
     (row.qty && row.selling_price)?row.total_price = row.qty * row.selling_price: row.total_price = 0;  
     frm.refresh_field('table_kpnf');
}

function calculate_total_cost(frm) {
    if (frm.doc.table_kpnf.length===0) {
        frm.doc.total_cost=total_cost=0
        return;
    }
    
    let total_cost = 0;
    frm.doc.table_kpnf.forEach(item => {
        total_cost += parseInt(item.total_price )|| 0;
    });
   frm.doc.total_cost=total_cost
}

frappe.ui.form.on("Custom Order",{
    refresh: function(frm) {
        console.log("Form refreshed");
        debugger; // JavaScript breakpoint
        a=1
        b=2
        console.log(a+b)
    }
})

