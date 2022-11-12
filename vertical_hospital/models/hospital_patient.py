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


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = "Patient Management"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    

    #Fields
    name = fields.Char('Internal Number', required=True, readonly=True, copy=False, tracking=True, default=_('New'))
    patient_name = fields.Char('Name and Last Name', required=True, readonly=False, copy=False, tracking=True)
    dni = fields.Char('DNI', required=True, trackig=True)
    datetime_start = fields.Datetime('Start Datetime', required=False, tracking=True, default=fields.Datetime.now())
    state = fields.Selection([
        ('draft', 'Draft'),
        ('start', 'Start'),
        ('done', 'Done')], string='Status', tracking=True, default='draft')

    #Relation fields
    treatments_ids = fields.Many2many('hospital.patient.treatments', 'rel_patient_treatments', 'patient_id', 'treatment_id', string="Treatments")
    active = fields.Boolean('Active', default=True)

    #Validacion de DNI
    #solo aceptara digitos
    @api.onchange('dni')
    def _onchange_patient_dni(self):
        if self.dni:
            if not str(self.dni).isdigit():
                return {
                    'value': {'dni': ''},
                    'warning': {'title': "Warning", 'message': _("The patient's DNI shouldn't contains letters, only number. Try again please.!")},
                }
    #Extends del metodo Create()
    #para asignar el numero de secuencia para cada paciente nuevo
    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.patient') or _('New')
        return super(HospitalPatient, self).create(vals)


    #Metodo para imprimir
    #reporte de detalle de pacientes
    #mediante el ir.actions.server
    def print_patient_details(self):
        return self.env.ref('vertical_hospital.action_report_patient').report_action(self)


HospitalPatient()