from frappe import _

def get_data():
    return [
        {
            "label": _("IVERP Report"),
            "items": [
                {
                    "type": "report",
                    "name": "Sales Order Listing",
		    "description": "SO Listing",
		    "doctype": "Sales Order",
		    "is_report_builder": True
                },
                {
                    "type": "report",
                    "name": "Purchase Receipt Listing",
                    "description": "Purchase Receipt Listing",
                    "doctype": "Purchase Receipt",
                    "is_report_builder": True
                },
		{
                    "type": "report",
                    "name": "Stock Availability",
		    "description": "Stock Availability by Location",
		"doctype": "IVERP REPORT",
		"is_query_report": True
                },
		{
                 "type": "report",
                 "name": "Accounts Payable",
                 "doctype": "Purchase Invoice",
                 "is_query_report": True
                 }


		]
}]
