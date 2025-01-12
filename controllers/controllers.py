# -*- coding: utf-8 -*-
# from odoo import http


# class /opt/odoo/odoo17CustomAddons/vendorPortal(http.Controller):
#     @http.route('//opt/odoo/odoo_17_custom_addons/vendor_portal//opt/odoo/odoo_17_custom_addons/vendor_portal', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//opt/odoo/odoo_17_custom_addons/vendor_portal//opt/odoo/odoo_17_custom_addons/vendor_portal/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('/opt/odoo/odoo_17_custom_addons/vendor_portal.listing', {
#             'root': '//opt/odoo/odoo_17_custom_addons/vendor_portal//opt/odoo/odoo_17_custom_addons/vendor_portal',
#             'objects': http.request.env['/opt/odoo/odoo_17_custom_addons/vendor_portal./opt/odoo/odoo_17_custom_addons/vendor_portal'].search([]),
#         })

#     @http.route('//opt/odoo/odoo_17_custom_addons/vendor_portal//opt/odoo/odoo_17_custom_addons/vendor_portal/objects/<model("/opt/odoo/odoo_17_custom_addons/vendor_portal./opt/odoo/odoo_17_custom_addons/vendor_portal"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/opt/odoo/odoo_17_custom_addons/vendor_portal.object', {
#             'object': obj
#         })

