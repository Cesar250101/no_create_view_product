# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class no_create_view_product(models.Model):
#     _name = 'no_create_view_product.no_create_view_product'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100