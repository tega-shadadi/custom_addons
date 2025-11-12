from odoo import models, fields

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    rfq_vendor_ids = fields.One2many(
        'rfq.vendor', 'order_id', string="RFQ Vendors"
    )

class RFQVendor(models.Model):
    _name = 'rfq.vendor'
    _description = 'RFQ Vendor'

    order_id = fields.Many2one('purchase.order', string="RFQ")
    vendor_id = fields.Many2one('res.partner', string="Vendor", domain=[('supplier_rank','>',0)])
    bid_amount = fields.Float(string="Bid Amount")
