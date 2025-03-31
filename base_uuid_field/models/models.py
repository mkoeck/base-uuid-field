from odoo import models, api, fields

class IrModelFields(models.Model):
    _inherit = 'ir.model.fields'

    ttype = fields.Selection(selection_add=[
        ('uuid', 'UUID'),
    ], ondelete={'uuid': 'cascade'})