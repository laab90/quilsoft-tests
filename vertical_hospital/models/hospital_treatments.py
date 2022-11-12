# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import datetime
from dateutil.relativedelta import relativedelta

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.osv import expression
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.tools.float_utils import float_compare
from odoo.exceptions import AccessError, UserError, ValidationError
from odoo.tools.misc import formatLang, get_lang

from dateutil import rrule


class HospitalPatientTreatments(models.Model):
    _name = 'hospital.patient.treatments'
    _description = "Patient Treatments Management"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Treatments', required=True, tracking=True, copy=True)
    code = fields.Char('Treatment Code', required=False, tracking=True, copy=True)
    doctor = fields.Char('Doctor', required=False, tracking=True, copy=True)

    active = fields.Boolean('Active', default=True)

    #Validacion de codigo
    #para que no contenga la cadana '026'
    @api.onchange('code')
    def _onchange_treatment(self):
        if self.code:
            if '026' in self.code:
                return {
                    'value': {'code': ''},
                    'warning': {'title': "Warning", 'message': _("Treatment code couldn't contains '026'. Try again, please.!")},
                }

HospitalPatientTreatments()