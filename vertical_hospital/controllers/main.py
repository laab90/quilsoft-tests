
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import base64
import json


from odoo import http, SUPERUSER_ID, _
from odoo.http import request, Response, JsonRequest

import logging
_logger = logging.getLogger(__name__)

class HospitalController(http.Controller):

    #Alternativa para el response de json RPC
    #para quitar los valores que traer el response
    #y solo enviar los valores del json resultante
    def alternative_json_response(self, result=None, error=None):
        response = {}
        if error is not None:
            response = error
        if result is not None:
            response = result
        mime = 'application/json'
        body = json.dumps(response)
        return Response(
            body, status=error and error.pop('http_status', 200) or 200,
            headers=[('Content-Type', mime), ('Content-Length', len(body))]
        )

    #Endpoint para consulta de pacientes
    #basado en su numero de secuencia/registro del paciente
    @http.route('/pacientes/consulta', methods=['POST'], type='json', auth='public', csrf=False)
    def get_patient_information(self, **kw):
        result = {}
        try:
            request._json_response = self.alternative_json_response.__get__(request, JsonRequest)
            body = request.jsonrequest
            patient = request.env['hospital.patient'].sudo().search([('name', '=', body.get('secuencia'))], limit=1)
            if not request.env.company.active_endpoint:
                return {'error': _('The web service for patient consultation is not active, consult your system administrator.')}
            if patient:
                _logger.info('**************Patient Object*******************')
                _logger.info(patient)
                result = {
                    'seq': patient.name,
                    'name': patient.patient_name,
                    'dni': patient.dni,
                    'state': patient.state,
                }
                _logger.info('**************Json Result*******************')
                _logger.info(result)
            else:
                result = {
                    'error': _("There isn't patient record with that sequence number.")
                }
        except Exception as e:
            result = {'errror': e}
            _logger.info('**************Json Error Result*******************')
            _logger.info(result)
        return result