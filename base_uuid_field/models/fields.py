from odoo import fields, _
from odoo.exceptions import ValidationError
from uuid import UUID as _UUID

def try_convert_to_uuid(value):
    """
    Helper function to convert a value to UUID.
    """
    if value and not isinstance(value, _UUID):
        try:
            value = _UUID(value)
        except ValueError:
            raise ValidationError(_("Invalid UUID value: %s. UUIDs should be in format d1d27475-ae70-4dd1-be55-6db42c83de7a (with or without dashes)", value))
    return value

class UUID(fields.Field[_UUID]):
    type = 'uuid'
    _column_type = ('uuid', 'uuid')

    def convert_to_column(self, value, record, values=None, validate=True):
        value = try_convert_to_uuid(value)
        return super().convert_to_column(value, record, values, validate)

    def convert_to_column_insert(self, value, record, values=None, validate=True):
        value = try_convert_to_uuid(value)
        return super().convert_to_column_insert(value, record, values, validate)

    def convert_to_column_update(self, value, record):
        return super().convert_to_column_update(value, record)

    def convert_to_cache(self, value, record, validate=True):
        value = try_convert_to_uuid(value)
        return super().convert_to_cache(value, record, validate)

    def convert_to_record(self, value, record):
        return super().convert_to_record(value, record)

    def convert_to_record_multi(self, values, records):
        return super().convert_to_record_multi(values, records)

    def convert_to_read(self, value, record, use_display_name=True):
        return super().convert_to_read(value, record, use_display_name)

    def convert_to_write(self, value, record):
        return super().convert_to_write(value, record)

    def convert_to_export(self, value, record):
        if isinstance(value, _UUID):
            value = str(value)
        return super().convert_to_export(value, record)

    def convert_to_display_name(self, value, record):
        return super().convert_to_display_name(value, record)

fields.UUID = UUID