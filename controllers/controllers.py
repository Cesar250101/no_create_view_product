# -*- coding: utf-8 -*-
from odoo import http

# class NoCreateViewProduct(http.Controller):
#     @http.route('/no_create_view_product/no_create_view_product/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/no_create_view_product/no_create_view_product/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('no_create_view_product.listing', {
#             'root': '/no_create_view_product/no_create_view_product',
#             'objects': http.request.env['no_create_view_product.no_create_view_product'].search([]),
#         })

#     @http.route('/no_create_view_product/no_create_view_product/objects/<model("no_create_view_product.no_create_view_product"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('no_create_view_product.object', {
#             'object': obj
#         })