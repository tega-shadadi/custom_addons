{
    'name': 'Purchase Request',
    'version': '1.0',
    'summary': 'Employees create purchase requests that procurement converts to RFQs',
    'description': "Simple Purchase Request module: create requests, submit, and generate RFQs.",
    'category': 'Purchases',
    'author': 'Shadadi',
    'license': 'LGPL-3',
    'depends': ['base', 'purchase', 'hr'],  # 
    'data': [
        'security/ir.model.access.csv',
        'views/purchase_request_views.xml',
        
        
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
