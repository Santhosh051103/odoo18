from odoo import fields, models


class AccountMoveContact(models.Model):
    _inherit = 'account.move'

    vendor_phone = fields.Char(related='partner_id.phone', string='Phone')
    vendor_email = fields.Char(related='partner_id.email', string='Email')
    vendor_address = fields.Char(related='partner_id.contact_address', string='Address')
