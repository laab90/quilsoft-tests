# -*- coding: utf-8 -*-

{
    'name': 'Hospital Management',
    'version': '1.01.1',
    'category': 'Others',
    'sequence': 1,
    'summary': 'Hospital Management',
    'description': "Hospital Management",
    'author':  "Luis Aquino",
    'support': "Luis Aquino -> laquinobarrientos@gmail.com",
    'depends': ['base_setup'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/menuitems.xml',
        'views/hospital_treatments_view.xml',
        'views/hospital_patient_view.xml',
        'views/res_config_settings_view.xml',
        'report/report_patient_tmpl.xml',
        'report/reports.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
