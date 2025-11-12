{
    'name': 'Purchase Multi Vendor',
    'version': '1.0',
    'category': 'Purchases',
    'summary': 'Allows assigning multiple vendors to one RFQ',
    'description': """
        This module extends the Purchase module to support multiple vendors
        per Request for Quotation (RFQ). Users can select several suppliers
        for a single RFQ and track them through the purchase process.
    """,
    'author': 'Shadadi Tega',
    'depends': ['purchase'],  # required base module
    'data': [
        'security/ir.model.access.csv',
        'views/purchase_order_view.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
