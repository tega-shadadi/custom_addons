from odoo import models, fields, api
from odoo.exceptions import UserError

class PurchaseBid(models.Model):
    _name = 'purchase.bid'
    _description = 'Vendor Bid'

    rfq_id = fields.Many2one('purchase.order', string="RFQ")
    rfq_vendor_id = fields.Many2one('res.partner', string="Vendor")
    amount = fields.Float(string="Bid Amount", required=True)
    status = fields.Selection([('pending', 'Pending'), ('winner', 'Winner')], default='pending')

    def select_winning_bid(self):
        self.status = 'winner'
        self.rfq_id.state = 'purchase'
        self.rfq_id.bid_ids.filtered(lambda b: b != self).write({'status': 'pending'})

    def action_submit_bid(self):
        if self.amount <= 0:
            raise UserError("Bid amount must be greater than zero")
        self.status = 'pending'
