{
    'name': 'Website Service Desk',
    'category': 'Service Desk',
    'summary': 'Website UI for Service Desk',
    'author': "Center of Research and Development",
    'website': "https://crnd.pro",
    'license': 'LGPL-3',
    'version': '12.0.1.53.0',

    'depends': [
        'mail',
        'website',
        'website_mail',
        'crnd_service_desk',
    ],
    'data': [
        'security/security.xml',
        'templates/templates.xml',
        'templates/templates_request_page.xml',
        'templates/templates_request_new_page.xml',
        'views/request_type_view.xml',
        'views/request_stage_route.xml',
        'views/request_category_view.xml',
        'views/request_kind.xml',
        'views/request_request.xml',
        'views/res_config_settings.xml',
        'data/website_data.xml',
        'data/request_type_incident.xml',
    ],
    'demo': [
        'demo/demo_res_users.xml',
        'demo/demo_category.xml',
        'demo/request_kind.xml',
        'demo/demo_generic_type.xml',
        'demo/demo_upgrade_type.xml',
        'demo/demo_request_type_seq.xml',
        'demo/demo_bug_report_type.xml',
    ],
    'qweb': [
        'static/src/xml/templates.xml',
    ],
    'images': ['static/description/banner.gif'],
    'installable': True,
    'auto_install': False,
}
