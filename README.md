 Purchase Request and RFQ Workflow Overview
_______________________________________________


This module extends Odoo’s purchasing functionality by introducing a Purchase Request process and a customized Request for Quotation (RFQ) workflow. It is designed for organizations where employees submit purchase requests to the Procurement department, which then prepares and manages RFQs based on those requests.

Features Implemented

1. RFQ Management

Procurement staff can prepare RFQs from purchase requests.

Each RFQ includes vendor details, items, and expected delivery.

Added state tracking for RFQs (New, Offer Received, Offer Accepted, Cancelled, Sold).

Streamlined form views and XML updates for improved usability.

2. Vendor Bid Handling (In Progress)

Planned functionality: vendors will be able to submit bids in response to RFQs.

The system will then allow the procurement officer to compare and select the winning vendor.

Once a winner is selected, the main partner_id on the RFQ will be automatically updated to reflect the selected vendor.

Upcoming Features

Vendor Portal Integration: Allow vendors to submit offers directly.

Bid Comparison View: Display vendor quotes side by side for selection.

Automatic Purchase Order Creation: Generate a Purchase Order from the accepted bid.

Email Notifications: Notify vendors upon RFQ publishing or selection.

 Technical Notes
____________________

Models

purchase.request: Handles internal purchase requests.

purchase.order (inherited): Modified to integrate with purchase requests.


  Views
__________

view_purchase_order.xml — Updated RFQ interface.



Dependencies

Odoo 18.0

purchase module


 Installation
_______________

Copy the module folder to your Odoo addons directory.

Update the app list:

odoo -u all


Activate developer mode and install the Purchase Request and RFQ Workflow module.

Author

Tega Shadady