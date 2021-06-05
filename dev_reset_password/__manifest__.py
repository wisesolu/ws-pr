# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd (<http://www.devintellecs.com>).
#
#    For Module Support : devintelle@gmail.com  or Skype : devintelle
#
##############################################################################

{
    'name': 'Reset Users Password',
    'version': '14.0.1.0',
    'sequence': 1,
    'category': 'Generic Modules/Tools',
    'description':
        """
odoo apps will send reset password link mail to the users

Reset Users Password
Odoo Reset Users Password
Reset password
Odoo reset password
Reset Password for users
Odoo Reset Password for users
Send link for reset password by mail to all users
Odoo Send link for reset password by mail to all users
Register and reset password
Odoo Register and reset password
User password
Odoo user password
User password reset
Odoo user password reset


    """,
    'summary': 'odoo apps will send reset password link mail to the users, reset password,Reset Password for users, autot password, send reset password request',
    'author': 'DevIntelle Consulting Service Pvt.Ltd',
    'website': 'http://www.devintellecs.com',
    'depends': ['mail', 'auth_signup'],
    'data': [
        'security/ir.model.access.csv',
        'views/dev_password_cron.xml',
        'wizard/dev_password_view.xml',
        ],
    'demo': [],
    'test': [],
    'css': [],
    'qweb': [],
    'js': [],
    'images': ['images/main_screenshot.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'price':12.0,
    'currency':'EUR',
    'live_test_url':'https://youtu.be/YlQ71tJPZ3Q', 
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
