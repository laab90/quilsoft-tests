# -*- coding: utf-8 -*-

from odoo import fields, models

class ResCompany(models.Model):
    _inherit = "res.company"

    active_endpoint = fields.Boolean('Active Endpoint', default=True)

ResCompany()

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    active_endpoint = fields.Boolean('Active Endpoint', readonly=False, related="company_id.active_endpoint")

ResConfigSettings()