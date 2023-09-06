# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Sales"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "doctype",
					"name": "Lead",
					"description": _("Database of potential customers."),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Customer",
					"description": _("Customer Database."),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Quotation",
					"description": _("Quotes to Leads or Customers."),
					"onboard": 1,
					"dependencies": ["Item", "Customer"],
				},
				{
					"type": "doctype",
					"name": "Sales Order",
					"description": _("Confirmed orders from Customers."),
					"onboard": 1,
					"dependencies": ["Item", "Customer"],
				},
 					   ]},
						
						{
						
						
			"label": _("Stock Transactions"),
			"items": [
				{
					"type": "doctype",
					"name": "Pick List",
					"onboard": 1,
					"dependencies": ["Item"],
				},				
				{
					"type": "doctype",
					"name": "Delivery Note",
					"onboard": 1,
					"dependencies": ["Item", "Customer"],
				},
				{
					"type": "doctype",
					"name": "Delivery Trip"
				},


			]},
			{
						"label": _("Items and Warehouse"),
			"items": [
				{
					"type": "doctype",
					"name": "Item",
					"onboard": 1,
				},
								{
					"type": "doctype",
					"name": "Item Group",
					"icon": "fa fa-sitemap",
					"label": _("Item Group"),
					"link": "Tree/Item Group",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Price List",
				},
				{
					"type": "doctype",
					"name": "Item Price",
				},

			]
			},
			{
						"label": _("Serial No and Batch"),
			"items": [
				{
					"type": "doctype",
					"name": "Serial No",
					"onboard": 1,
					"dependencies": ["Item"],
				},
				{
					"type": "doctype",
					"name": "Batch",
					"onboard": 1,
					"dependencies": ["Item"],
				},
				{
					"type": "doctype",
					"name": "Warehouse",
					"onboard": 1,
				},

			]
	
	},
	]
	
