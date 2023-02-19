# -*- coding: utf-8 -*-
{
    'name': "bar",

    'summary': """
        Exam bar""",

    'description': """
        Exam about bar
    """,

    'author': "Nicolas",
    'website': "http://www.isca.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web_notify'],

    # always loaded
    'data': [
        'security/bar_security.xml',
        'security/ir.model.access.csv',
        'views/product_view.xml',
        'views/category_view.xml',
        'views/ingredient_view.xml',
        'views/order_view.xml',
        'views/register_view.xml',
        'views/invoice_view.xml',
        'views/invoicelines_view.xml',
        'report/invoice_report.xml',
        'views/menu.xml',
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
}
