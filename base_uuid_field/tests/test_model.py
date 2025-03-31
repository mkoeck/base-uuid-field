from odoo_test_helper import FakeModelLoader
from odoo.tests import TransactionCase
from uuid import uuid4, UUID

class TestModel(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.loader = FakeModelLoader(cls.env, cls.__module__)
        cls.loader.backup_registry()

        from .models import UuidTest

        cls.loader.update_registry((UuidTest,))

    @classmethod
    def tearDownClass(cls):
        cls.loader.restore_registry()
        super().tearDownClass()

    def test_ir_model_fields(self):
        """Test that the UUID field is correctly reflected in the ir.model.fields table."""
        field = self.env['ir.model.fields'].search([('name', '=', 'external_id'), ('model', '=', 'uuid.test')])
        self.assertEqual(field.ttype, 'uuid')

    def test_column_type(self):
        """Test that the UUID field has the correct column type in the database."""
        self.env.cr.execute("SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'uuid_test' AND column_name = 'external_id'")
        column = self.env.cr.fetchone()
        self.assertEqual(column[0], 'external_id')
        self.assertEqual(column[1], 'uuid')

    def test_create_from_string(self):
        uuid = '86223127-1c62-49f2-af41-9fba7c3ddde3'
        record = self.env['uuid.test'].create({'external_id': uuid})
        self.env.cr.execute("SELECT external_id FROM uuid_test WHERE id = %s", (record.id,))
        
        db_uuid = self.env.cr.fetchone()[0]
        self.assertEqual(record.external_id, UUID(uuid))
        self.assertIsInstance(record.external_id, UUID)
        self.assertEqual(db_uuid, uuid)

    def test_create_from_uuid(self):
        uuid = uuid4()
        record = self.env['uuid.test'].create({'external_id': uuid})
        self.env.cr.execute("SELECT external_id FROM uuid_test WHERE id = %s", (record.id,))
        
        db_uuid = self.env.cr.fetchone()[0]
        self.assertEqual(record.external_id, uuid)
        self.assertIsInstance(record.external_id, UUID)
        self.assertEqual(db_uuid, str(uuid))

    def test_write_from_string(self):
        uuid = '86223127-1c62-49f2-af41-9fba7c3ddde3'
        record = self.env['uuid.test'].create({'external_id': uuid})
        
        new_uuid = '86223127-1c62-49f2-af41-9fba7c3ddde4'
        record.external_id = new_uuid
        
        record.flush_recordset()

        self.assertEqual(record.external_id, UUID(new_uuid))
        self.assertIsInstance(record.external_id, UUID)

    def test_write_from_uuid(self):
        uuid = uuid4()
        record = self.env['uuid.test'].create({'external_id': uuid})

        new_uuid = uuid4()
        record.external_id = new_uuid

        record.flush_recordset()

        self.assertEqual(record.external_id, new_uuid)
        self.assertIsInstance(record.external_id, UUID)

    def test_convert_to_export(self):
        uuid = uuid4()
        records = self.env['uuid.test'].create([{'external_id': uuid}, {'external_id': None}])

        export_value = records.export_data(['external_id'])
        self.assertEqual(export_value['datas'][0][0], str(uuid))
        self.assertEqual(export_value['datas'][1][0], '')

    def test_convert_to_display_name(self):
        uuid = uuid4()
        record = self.env['uuid.test'].create({'external_id': uuid})
        
        self.assertEqual(record.display_name, str(uuid))

    def test_convert_to_record_multi(self):
        uuid = uuid4()
        record = self.env['uuid.test'].create({'external_id': uuid})
        
        uuids = record.mapped('external_id')

        self.assertEqual(len(uuids), 1)
        self.assertEqual(uuids[0], uuid)
        self.assertIsInstance(uuids[0], UUID)