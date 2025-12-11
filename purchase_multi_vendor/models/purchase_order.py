from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.addons.purchase.models.purchase_order import PurchaseOrder as PurchaseOrderBase
from odoo.exceptions import ValidationError


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    partner_id = fields.Many2one(required=False)  # keep optional
    rfq_vendor_ids = fields.Many2many(
        'res.partner',
        string="Select Vendors",
        help="Select multiple vendors to invite for this RFQ.",
        
    )

    @api.constrains('rfq_vendor_ids')
    def _check_vendor_ids(self):
        for rec in self:
            if not rec.rfq_vendor_ids:
                raise ValidationError("Please select at least one vendor.")
            

    def action_rfq_send(self):
        """Send RFQ emails to all selected vendors without creating multiple POs"""
        template = self.env.ref('purchase.email_template_edi_purchase')

        for order in self:
            if not order.rfq_vendor_ids:
                raise UserError("Please select at least one vendor before sending RFQ.")

            # Set primary vendor (required by Odoo)
            if not order.partner_id:
                order.partner_id = order.rfq_vendor_ids[0]

            # Call original Odoo logic once (to trigger RFQ workflow)
            super(PurchaseOrder, order).action_rfq_send()

            # Send emails to all selected vendors
            for vendor in order.rfq_vendor_ids:
                if vendor.email:
                    template.send_mail(
                        order.id,
                        force_send=True,
                        email_values={'email_to': vendor.email}
                    )

            # Manually update PO state if needed
            order.state = 'sent'  # or the correct RFQ state

            """Override Send RFQ to send to all selected vendors"""
            template = self.env.ref('purchase.email_template_edi_purchase')
        
            for order in self:
                if not order.rfq_vendor_ids:
                    raise UserError("Please select at least one vendor before sending RFQ.")
                
                # Set partner_id to first vendor (required by Odoo)
                order.partner_id = order.rfq_vendor_ids[0]

                for vendor in order.rfq_vendor_ids:
                    # Set partner_id for Odoo logic
                    order.partner_id = vendor

                    # Set Vendor Reference
                    order.partner_ref = vendor.ref or ''

                    # Call original Odoo logic for this vendor
                    super(PurchaseOrder, order).action_rfq_send()

                    # Send email explicitly (optional, Odoo may already do this)
                    if vendor.email:
                        template.send_mail(
                            order.id,
                            force_send=True,
                            email_values={'email_to': vendor.email}
                        )
                # Update PO state manually
                order.state = 'sent'

                
                 

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



