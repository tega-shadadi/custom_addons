{
    'name': 'Purchase Request',
    'version': '1.0',
    'summary': 'Employees create purchase requests that procurement converts to RFQs',
    'description': "Simple Purchase Request module: create requests, submit, and generate RFQs.",
    'category': 'Purchases',
    'author': 'Shadadi',
    'license': 'LGPL-3',
    'depends': ['base', 'purchase'],  # add 'purchase_multi_vendor' if you have that module
    'data': [
        'security/ir.model.access.csv',
        'views/purchase_request_views.xml',
        # menus after views (if you split files, ensure sequence)
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
