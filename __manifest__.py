# -*- coding: utf-8 -*-
{
    'name': "no_create_view_product",

    'summary': """
Desactiva la opción de poder crear productos en las líneas de los documentos de
venta, compras e inventario""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Method ERP",
    'website': "http://www.method.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','purchase','mrp_repair'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
