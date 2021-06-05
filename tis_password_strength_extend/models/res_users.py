# -*- coding: utf-8 -*-
# This module and its content is copyright of Technaureus Info Solutions Pvt. Ltd.
# - © Technaureus Info Solutions Pvt. Ltd 2020. All rights reserved.

from odoo import api, fields, models, _
from odoo.exceptions import UserError
import re


class ResUsers(models.Model):
    _inherit = 'res.users'

    restrict_weak_password = fields.Boolean(string='Block Weak Password Creation')
    min_password_strength = fields.Integer(string='Minimum Strength Of Password')

    @api.model
    def change_password(self, old_passwd, new_passwd):
        """Change current user password. Old password must be provided explicitly
        to prevent hijacking an existing user session, or for cases where the cleartext
        password is not used to authenticate requests.

        :return: True
        :raise: odoo.exceptions.AccessDenied when old password is wrong
        :raise: odoo.exceptions.UserError when new password is not set or empty
        """

        restrict_weak_password = self.env['ir.config_parameter'].sudo().get_param('tis_password_strength_extend.weak_password')
        min_password_strength = self.env['ir.config_parameter'].sudo().get_param(
            'tis_password_strength_extend.weak_password_strength')
        self.check(self._cr.dbname, self._uid, old_passwd)
        if new_passwd:
            # use self.env.user here, because it has uid=SUPERUSER_ID
            if restrict_weak_password:
                password = new_passwd
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
                if password_strength < int(min_password_strength):
                    raise UserError(_("Your password must have a minimum strength"))
            return self.env.user.write({'password': new_passwd})
        raise UserError(_("Setting empty passwords is not allowed for security reasons!"))
