from odoo import http
from odoo.http import request

class PurchasePortalController(http.Controller):

    @http.route('/my/bids', type='http', auth='user', website=True)
    def portal_bids(self, **kwargs):
        bids = request.env['purchase.bid'].search([
            ('rfq_vendor_id', '=', request.env.user.partner_id.id)
        ])
        return request.render('purchase_multi_vendor.portal_bid_list', {
            'bids': bids,
        })
