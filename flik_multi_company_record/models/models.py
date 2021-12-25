# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductCategoryMultiCompany(models.Model):
    _inherit = "product.category"

    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env['res.company']._company_default_get('product_category_multi_company'))


class ResBankMultiCompany(models.Model):
    _inherit = "res.bank"

    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env['res.company']._company_default_get('res_bank_multi_company'))


class ResPartnerMultiCompany(models.Model):
    _inherit = "res.partner"