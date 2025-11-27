If you'd like changes to tone, length, or additional sections (screenshots, role/permissions notes, or developer setup), tell me which parts to expand and I'll update the README accordingly.
# Purchase Request & Purchase Multi-Vendor

This repository contains Odoo 18 add-ons that extend the standard purchasing workflow by introducing a Purchase Request process and a multi-vendor RFQ (Request for Quotation) workflow. These modules help organizations where employees raise purchase requests and procurement manages RFQs, collects vendor bids, and selects winning offers.

## Modules Included

- `purchase_request`: Capture employee purchase requests and convert them into RFQs.
- `purchase_multi_vendor`: Manage multi-vendor RFQs, collect vendor bids, and select winners.

## Overview

The solution separates the request and procurement responsibilities:

- Employees submit purchase requests (product, quantity, requester, justification).
- Procurement converts approved requests into RFQs and invites multiple vendors to bid.
- Vendors submit bids; procurement compares offers and selects a winner.
- The winning bid becomes the supplier on the RFQ and can be confirmed into a Purchase Order.

## Key Features

- Create and manage purchase requests with reference, requester, product, quantity, and status.
- Convert a request to an RFQ with a single click.
- Invite multiple vendors to an RFQ and collect vendor bids (`bid_ids`).
- Select a winning vendor; the RFQ `partner_id` updates automatically.
- RFQ state progression: New → Offer Received → Offer Accepted → Order Confirmed → Cancelled.

## User Workflow

1. Create a Purchase Request
   - Navigate to **Purchase Requests → Requests** and click **Create**. Fill in required fields and save.

2. Convert Request to RFQ
   - Click **Create RFQ** on the request form to generate a linked RFQ.

3. Add Vendors to RFQ
   - In the RFQ form add vendors to the `Vendors` (many2many `vendor_ids`) field.
   - Invite vendors to bid manually or via your vendor portal (if enabled).

4. Vendors Submit Bids
   - Vendor bids are stored under the `Vendor Bids` tab. Each bid includes amount, currency, and comments.

5. Compare and Select Winner
   - Review bids and click **Select Winner** on the chosen bid. That bid's status becomes Winner, and the RFQ `partner_id` updates to the selected vendor.

6. Confirm Purchase
   - Confirm the RFQ into a Purchase Order. The selected vendor becomes the supplier for the order.

## Installation

1. Clone this repository into your Odoo addons directory:

```bash
git clone https://github.com/tega-shadadi/custom_addons.git
```

2. Restart Odoo and update the Apps list. Then install the `Purchase Request` and `Purchase Multi-Vendor` modules from Apps.

Example (environment dependent):

```bash
# restart your Odoo server and update modules
# (replace with your environment-specific commands)
odoo -u all
```

## Technical Notes

- Tested with: Odoo 18
- Dependencies: Odoo core `purchase` and `hr` module
- Important models: `purchase.request` (new), `purchase.order` (extended), and vendor bid models (e.g., `purchase.bid`).
- Views: `purchase_order_view_v2.xml` includes RFQ/bid UI changes.


## Author

Tega Shadadi

