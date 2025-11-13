from odoo import models, fields, api
from odoo.exceptions import UserError

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    rfq_vendor_ids = fields.Many2many(
        'res.partner',
        string="Select Vendors",
        help="Select multiple vendors to invite for this RFQ."
    )

    bid_ids = fields.One2many(
        'purchase.bid',
        'rfq_id',
        string="Vendor Bids"
    )

    def select_winning_bid(self, bid_id):
        """Called from UI button — set a bid as winner and confirm."""
        bid = self.env['purchase.bid'].browse(bid_id)
        self.ensure_one()

        if not bid:
            raise UserError("No bid found with that ID.")

        bid.select_winning_bid()
