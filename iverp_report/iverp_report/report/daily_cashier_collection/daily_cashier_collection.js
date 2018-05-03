// Copyright (c) 2016, IVERIFII SOLUTIONS SB and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Daily Cashier Collection"] = {
	"filters": [
{
            "fieldname":"selected_date",
            "label": __("Selected Date"),
            "fieldtype": "Date Range",
            "reqd": true
        },
        {
            "fieldname":"company",
            "label": __("Company"),
            "fieldtype": "Link",
            "options": "Company",
            "default": frappe.defaults.get_user_default("Company")
        },
        {
            "fieldname":"location",
            "label": __("Location"),
            "fieldtype": "Link",
            "options": "Warehouse"
        },
        {
            "fieldname":"owner",
            "label": __("Owner"),
            "fieldtype": "Link",
            "options": "User",
            "defaults": user
}
	]
}
