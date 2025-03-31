from odoo import models, api, fields

class UuidTest(models.Model):
    _name = 'uuid.test'
    _description = 'UUID Test'
    _rec_name = 'external_id'
    _order = 'external_id'

    external_id = fields.UUID()
    other_field = fields.Char(string='Other Field')