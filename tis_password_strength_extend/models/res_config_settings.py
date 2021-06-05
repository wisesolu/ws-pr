# -*- coding: utf-8 -*-
# This module and its content is copyright of Technaureus Info Solutions Pvt. Ltd.
# - © Technaureus Info Solutions Pvt. Ltd 2020. All rights reserved.

from ast import literal_eval

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    restrict_weak_password = fields.Boolean(string='Block Weak Password Creation', config_parameter='tis_password_strength_extend.weak_password')
    min_password_strength = fields.Integer(string='Minimum Strength Of Password', config_parameter='tis_password_strength_extend.weak_password_strength')





