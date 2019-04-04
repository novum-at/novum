// Copyright (c) 2019, novum-locations and contributors
// For license information, please see license.txt

frappe.ui.form.on('Locations', {
	refresh: function(frm) {
		frappe.call({
			method: 'novum.novum.doctype.locations.locations.get_room_overview',
			args: {
				'location': frm.doc.name
			},
			callback: function(r) {
				if (r.message) {
					cur_frm.set_df_property('room_overview','options',r.message);
				}
			}
		});
	}
});
