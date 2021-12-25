# -*- coding: utf-8 -*-
{
    'name': "Multi Company Record Rule",

    'summary': """
        Show Company On Product Category, Bank and Partner Apply Record Rule on base of Company
         """,

    'description': """
        Show Company On Product Category, Bank and Partner Apply Record Rule on base of Company
    """,

    'author': "Viltco",
    'website': "http://www.viltco.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'stock',
    'version': '14.0.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock', 'contacts'],

    # always loaded
    'data': [
        'views/views.xml',
    ],
}
