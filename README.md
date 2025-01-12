Vendor Registration Module

This module enables vendors to register themselves on the portal and allows admins to manage and approve vendor registrations.
Installation Guide

    Place this module in your custom addons directory.
    Restart your Odoo instance.
    Install the module from the Odoo Apps menu.

Portal User Access

    Access the portal at host:port/my.
    Portal users will only see the "Register a new vendor" menu option.

Internal User Access

Internal users (admins) will have access to two main menu options:

    Register a new vendor
    View the list of vendors

Features for Vendors

    Self-Registration: Vendors can register themselves through the portal.
    Mandatory Field Validation: The system ensures that all required fields are filled out during registration.
    Field Uniqueness: The system checks for uniqueness in certain fields (e.g., company email).
    Field Validation: The system validates critical fields like:
        Tax Identification Number (TIN)
        Trade License Number
        Expiry Date (ensures the date is not in the past)
    Demo Supplier Creation: Upon registration, the system creates a demo vendor under review.

Features for Admins

    New Vendor Registration Menu: A new menu is available under Purchase > Order > Vendor Registration.
    Vendor Management: Admins can view the list of registered vendors and approve or reject them.
    Vendor Approval: Upon approval:
        A new vendor record is created.
        A new user is generated with the vendor’s email and password (email and password are the same).
        The vendor receives an email with their login credentials.

Notes

    Ensure that your email configuration is properly set up to send login credentials to approved vendors.
    Admins can manage vendor approvals directly from the Odoo backend.