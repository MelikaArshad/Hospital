import unittest
from model.medical_record import MedicalRecord
from controller import MedicalRecordController
from tools import Logger

class TestMedicalRecordController(unittest.TestCase):
    def setUp(self):
        self.logger = Logger()

    def test_save_medical_record(self):
        status, message = MedicalRecordController.save(
            1001,"Test Patient","Test Doctor",
            "Test Staff","Test Dept","Visit","Test check")
        self.assertTrue(status)
        self.assertIn("Successfully", message)
        self.logger.info("Tested save_medical_record")

    def test_update_medical_record(self):
        status, message = MedicalRecordController.update(1001,"Updated check")
        self.assertTrue(status)
        self.assertIn("Updated", message)
        self.logger.info("Tested update_medical_record")

    def test_update_nonexistent_medical_record(self):
        status, message = MedicalRecordController.update(999999,"Nonexistent")
        self.assertFalse(status)
        self.logger.info("Tested update_nonexistent_medical_record")

    def test_delete_medical_record(self):
        status, message = MedicalRecordController.delete(1001)
        self.assertTrue(status)
        self.assertIn("Deleted", message)
        self.logger.info("Tested delete_medical_record")

    def test_find_all_medical_records(self):
        records = MedicalRecordController.find_all()
        self.assertIsInstance(records, list)
        self.logger.info("Tested find_all_medical_records")

    def test_find_by_unit_no_medical_record(self):
        status, record = MedicalRecordController.find_by_unit_no(1001)
        self.assertTrue(status)
        self.logger.info("Tested find_by_unit_no_medical_record")

    def test_find_by_unit_no_not_found(self):
        status, record = MedicalRecordController.find_by_unit_no(999999)
        self.assertFalse(status)
        self.logger.info("Tested find_by_unit_no_not_found")

    def test_find_by_unit_no_non_existent_record(self):
        status, record = MedicalRecordController.find_by_unit_no(999999)
        self.assertFalse(status)
        self.logger.info("Tested find_by_unit_no_non_existent_record")

    def test_find_by_name_medical_record(self):
        records = MedicalRecordController.find_by_name("Test")
        self.assertIsInstance(records, list)
        self.logger.info("Tested find_by_name_medical_record")

if __name__ == '__main__':
    unittest.main()



