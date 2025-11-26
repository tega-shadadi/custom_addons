from odoo import models, fields, api

class PurchaseRequest(models.Model):
    _name = "purchase.request"
    _description = "Purchase Request"

    name = fields.Char(string="Request Reference", required=True)
    employee_id = fields.Many2one('hr.employee', string="Employee", required=True)
    product_id = fields.Many2one('product.product', string="Product", required=True)
    quantity = fields.Float(string="Quantity", required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('rfq_generated', 'RFQ Generated'),
    ], string="Status", default='draft', required=True)

    def action_create_rfq(self):
        """Convert request to RFQ using the multi-vendor RFQ module"""
        PurchaseOrder = self.env['purchase.order']
        for request in self:
            # Use the first supplier of the product as vendor
            vendor_id = request.product_id.seller_ids[:1].partner_id.id if request.product_id.seller_ids else False
            if not vendor_id:
                raise UserError("The product has no supplier. Please assign a vendor before creating RFQ.")
            
            po = PurchaseOrder.create({
                'partner_id': vendor_id,
                'order_line': [(0, 0, {
                    'product_id': request.product_id.id,
                    'product_qty': request.quantity,
                    'price_unit': request.product_id.standard_price,
                })],
            })
            request.state = 'rfq_generated'
        return True
