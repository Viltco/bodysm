# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "E Invoicing",
    "version": "14.0.1.0.0",
    "category": "Techistan Project",
    "website": "https://techistan.com",
    "author": "Techistan",
    "license": "LGPL-3",
    "application": True,
    "installable": True,
    "depends": ["base", "account"],
    "data": [
        "views/account_move.xml",
        "views/base_company.xml",
        "reports/report_invoice_document.xml",
    ],
}
