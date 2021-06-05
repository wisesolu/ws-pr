# -*- coding: utf-8 -*-
# This module and its content is copyright of Technaureus Info Solutions Pvt. Ltd.
# - © Technaureus Info Solutions Pvt. Ltd 2020. All rights reserved.
{
    'name': 'User Password Strength - Restrict Weak Password',
    'version': '14.0.0.0',
    'sequence': 1,
    'category': 'Extra Tools',
    'summary': 'User Password Strength And Restrict Weak Password',
    'author': 'Technaureus Info Solutions Pvt. Ltd.',
    'website': 'http://www.technaureus.com/',
    'price': 34.99,
    'currency': 'EUR',
    'license': 'Other proprietary',
    'description': """
    User Password Strength And Restrict Weak Password
        """,
    'depends': ['auth_signup'],
    'data': [
        'views/password_strength_views.xml',
        'views/res_config_settings_views.xml',
    ],
    'images': ['images/main_screenshot.png'],
    'installable': True,
    'auto_install': False,
    'application': True,
    'live_test_url': 'https://www.youtube.com/watch?v=oC563O5g3H8'
}
