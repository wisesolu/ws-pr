# -*- coding: utf-8 -*-
# This module and its content is copyright of Technaureus Info Solutions Pvt. Ltd.
# - © Technaureus Info Solutions Pvt. Ltd 2020. All rights reserved.
import logging
import werkzeug

from odoo import http, _
from odoo.addons.auth_signup.models.res_users import SignupError
from odoo.addons.web.controllers.main import ensure_db, Home
from odoo.addons.base_setup.controllers.main import BaseSetup
from odoo.exceptions import UserError
from odoo.http import request
import re

_logger = logging.getLogger(__name__)


class AuthSignupHome(Home):

    def get_auth_signup_config(self):
        """retrieve the module config (which features are enabled) for the login page"""

        get_param = request.env['ir.config_parameter'].sudo().get_param
        return {
            'signup_enabled': request.env['res.users']._get_signup_invitation_scope() == 'b2c',
            'reset_password_enabled': get_param('auth_signup.reset_password') == 'True',
            'restrict_weak_password': get_param('tis_password_strength_extend.weak_password'),
            'min_password_strength': get_param('tis_password_strength_extend.weak_password_strength'),
        }

    def do_signup(self, qcontext):
        """ Shared helper that creates a res.partner out of a token """
        values = {key: qcontext.get(key) for key in ('login', 'name', 'password', 'restrict_weak_password', 'min_password_strength')}
        if not values:
            raise UserError(_("The form was not properly filled in."))
        if values.get('password') != qcontext.get('confirm_password'):
            raise UserError(_("Passwords do not match; please retype them."))
        restrict = values.get('restrict_weak_password')
        min_strength = int(values.get('min_password_strength'))
        if restrict:
            password = values.get('password')
            if len(password) < 8:
                password_strength = 0
            if re.search("^((?=.*[a-z])|(?=.*[A-Z])|(?=.*[0-9]))(?=.{8,})",
                         password):
                password_strength = 10
            if re.search("^(((?=.*[a-z])(?=.*[A-Z]))|((?=.*[a-z])(?=.*[0-9]))|((?=.*[A-Z])(?=.*[0-9])))(?=.{8,})",
                         password):
                password_strength = 25
            if re.search("^((?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]))(?=.{8,})", password):
                password_strength = 50
            if re.search(
                    "^(((?=.*[a-z])(?=.*[0-9])(?=.*[!@#\$%\^&\*]))|((?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])))(?=.{8,})",
                    password):
                password_strength = 75
            if re.search("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})", password):
                password_strength = 100
            if password_strength < min_strength:
                raise UserError(_("Your password must have a minimum strength"))
        supported_lang_codes = [code for code, _ in request.env['res.lang'].get_installed()]
        lang = request.context.get('lang', '').split('_')[0]
        if lang in supported_lang_codes:
            values['lang'] = lang
        self._signup_with_values(qcontext.get('token'), values)
        request.env.cr.commit()
