from odoo import models, fields, api

class PurchaseBid(models.Model):
    _name = 'purchase.bid'
    _description = 'Vendor Bid'

    rfq_id = fields.Many2one(
        'purchase.order',
        string='RFQ',
        required=True,
        ondelete='cascade'
    )
    rfq_vendor_id = fields.Many2one(
        'res.partner',
        string='Vendor',
        required=True
    )
    amount = fields.Float(string='Bid Amount', required=True)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('winner', 'Winner')
    ], string='Status', default='draft')

    def select_winning_bid(self):
        """Set this bid as winner and update the RFQ's vendor."""
        for bid in self:
            # Mark as winner
            bid.status = 'winner'

            # Update main vendor on the RFQ
            bid.rfq_id.partner_id = bid.rfq_vendor_id

            # Optionally confirm the order
            bid.rfq_id.button_confirm()
