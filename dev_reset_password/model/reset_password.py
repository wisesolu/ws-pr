# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd (<http://www.devintellecs.com>).
#
#    For Module Support : devintelle@gmail.com  or Skype : devintelle
#
##############################################################################

from odoo import models


class set_password(models.Model):
    _name = 'set.password'
    _description = 'Set Password'

    def action_reset_password(self):
        user_ids = self.env['res.users'].search([])
        admin_group = self.env.ref('base.group_system')
        admins = []
        if admin_group and admin_group.users:
            admins = admin_group.users.ids
        if user_ids:
            for user in user_ids:
                if user.id not in admins:
                    if user.partner_id.email:
                        user.reset_password(user.partner_id.email)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: