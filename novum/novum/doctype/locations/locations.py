# -*- coding: utf-8 -*-
# Copyright (c) 2019, novum-locations and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Locations(Document):
	pass
	
@frappe.whitelist()
def get_room_overview(location):
	room_overview = '<div>'
	rooms = frappe.db.sql("""SELECT * FROM `tabRooms` WHERE `location` = '{location}'""".format(location=location), as_dict=True)
	for room in rooms:
		room_overview = room_overview + '<div class="row"><div class="col-xs-12">'
		room_overview = room_overview + '<h3>' + room.room_name + '</h3>'
		room_overview = room_overview + '<p><i class="fa fa-clone"></i> ' + str(room.room_area) + 'm<sup>2</sup></p>'
		room_overview = room_overview + '<table style="width: 100%;"><tr><th>Equipment</th><th>Fix</th><th>Mobil</th></tr>'
		equipments = frappe.db.sql("""SELECT * FROM `tabRoomequipment` WHERE `parenttype` = 'Rooms' AND `parentfield` = 'equipment'""", as_dict=True)
		for equipment in equipments:
			room_overview = room_overview + '<tr>'
			if equipment.mobil == 1:
				room_overview = room_overview + '<td>' + equipment.item + '</td><td><i class="fa fa-times"></i></td><td><i class="fa fa-check"></i></td></tr>'
			else:
				room_overview = room_overview + '<td>' + equipment.item + '</td><td><i class="fa fa-check"></i></i></td><td><i class="fa fa-times"></td></tr>'
		room_overview = room_overview + '</table></div></div>'
	room_overview = room_overview + '</div>'
	return room_overview