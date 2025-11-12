 Purchase Request and RFQ Workflow Overview
-------


This module extends Odoo’s purchasing functionality by introducing a Purchase Request process and a customized Request for Quotation (RFQ) workflow. It is designed for organizations where employees submit purchase requests to the Procurement department, which then prepares and manages RFQs based on those requests.

Features Implemented

1. RFQ Management

- Procurement can send RFQs to multiple vendors.
- Each vendor can submit their **bid amount** and details.
- Procurement can view all vendor bids in one place.
- A winning vendor can be selected manually, updating the main `partner_id` of the RFQ.
- State transitions for RFQ: **New → Offer Received → Offer Accepted → Sold → Cancelled**

2. Vendor Bid Handling (In Progress)

Planned functionality: vendors will be able to submit bids in response to RFQs.

The system will then allow the procurement officer to compare and select the winning vendor.

Once a winner is selected, the main partner_id on the RFQ will be automatically updated to reflect the selected vendor.

Upcoming Features
-------------------

Vendor Portal Integration: Allow vendors to submit offers directly.

Bid Comparison View: Display vendor quotes side by side for selection.

Automatic Purchase Order Creation: Generate a Purchase Order from the accepted bid.

Email Notifications: Notify vendors upon RFQ publishing or selection.

 Technical Notes
-------

Models

purchase.request: Handles internal purchase requests.

purchase.order (inherited): Modified to integrate with purchase requests.


  Views
-------

view_purchase_order.xml — Updated RFQ interface.



Dependencies

Odoo 18.0

purchase module


 Installation
-------

1. Clone the repository into your Odoo addons directory:

   ```bash
   git clone https://github.com/tega-shadadi/custom_addons.git


Copy the module folder to your Odoo addons directory.

Update the app list:

odoo -u all


Activate developer mode and install the Purchase Request and RFQ Workflow module.

USAGE
-------

Step 1: Click Create RFQ — this automatically generates a linked RFQ.

Select Vendors

In the RFQ form view, select multiple vendors under Vendors (Many2many field vendor_ids).

Each vendor will receive a copy of the RFQ or can be invited to bid manually.

Step 2: Vendors Submit Bids

Each vendor sends their bid amount and optional comments.

Procurement encodes these offers under the Vendor Bids tab.

Every entry is recorded in the bid_ids One2many list.

Step 3: Select the Winning Bid

In the Vendor Bids tab, click Select Winner beside the chosen vendor.

The bid’s status updates to Winner.

The main RFQ’s partner_id is automatically updated to the winning vendor.

You can proceed to confirm the purchase order.

Step 4: Complete Purchase

Validate or confirm the RFQ as usual.

The selected vendor becomes the supplier for the purchase order.

Author
--------

Tega Shadadi
