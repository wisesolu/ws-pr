# -*- coding: utf-8 -*-
# This module and its content is copyright of Technaureus Info Solutions Pvt. Ltd.
# - © Technaureus Info Solutions Pvt. Ltd 2020. All rights reserved.

from odoo import api, fields, models, _
from odoo.exceptions import UserError
import re


class ChangePasswordUser(models.TransientModel):
    _inherit = "change.password.user"

    password_strength = fields.Integer(string="Password Strength")
    password_complexity = fields.Char(string="Password Complexity", readonly=True)

    @api.onchange('new_passwd')
    def onchange_password_strength(self):
        for line in self:
            password = line.new_passwd
            if len(password) < 8:
                self.password_strength = 0
                self.password_complexity = "Weak"
            if re.search("^((?=.*[a-z])|(?=.*[A-Z])|(?=.*[0-9]))(?=.{8,})",
                         password):
                self.password_strength = 10
                self.password_complexity = "Very Poor"
            if re.search("^(((?=.*[a-z])(?=.*[A-Z]))|((?=.*[a-z])(?=.*[0-9]))|((?=.*[A-Z])(?=.*[0-9])))(?=.{8,})",
                         password):
                self.password_strength = 25
                self.password_complexity = "Poor"
            if re.search("^((?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]))(?=.{8,})", password):
                self.password_strength = 50
                self.password_complexity = "Good"
            if re.search(
                    "^(((?=.*[a-z])(?=.*[0-9])(?=.*[!@#\$%\^&\*]))|((?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])))(?=.{8,})",
                    password):
                self.password_strength = 75
                self.password_complexity = "Strong"
            if re.search("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})", password):
                self.password_strength = 100
                self.password_complexity = "Very Strong"

    def change_password_button(self):
        restrict_weak_password = self.env['ir.config_parameter'].sudo().get_param('tis_password_strength_extend.weak_password')
        min_password_strength = self.env['ir.config_parameter'].sudo().get_param(
            'tis_password_strength_extend.weak_password_strength')
        for line in self:
            if not line.new_passwd:
                raise UserError(_("Before clicking on 'Change Password', you have to write a new password."))
            if restrict_weak_password:
                if line.password_strength < int(min_password_strength):
                    raise UserError(_("Your password must have a minimum strength"))
            line.user_id.write({'password': line.new_passwd})
        # don't keep temporary passwords in the database longer than necessary
        self.write({'new_passwd': False})
