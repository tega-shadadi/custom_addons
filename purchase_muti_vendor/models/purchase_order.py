from odoo import models, fields

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    vendor_ids = fields.Many2many(
        'res.partner',                # Model to link to
        'purchase_order_vendor_rel',  # Relation table (optional)
        'order_id',                   # Current model FK in relation
        'partner_id',                 # Related model FK in relation
        string='Vendors',
        domain=[('supplier_rank', '>', 0)],  # Only vendors
    )
