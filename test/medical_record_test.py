import unittest
from model.medical_record import MedicalRecord
from controller.medical_record_controller import MedicalRecordController
from tools.logger import Logger

class TestMedicalRecordController(unittest.TestCase):
    def setUp(self):
        self.logger = Logger()
        self.test_record = MedicalRecord(
            unit_no=1001,
            full_name="Ahmad Mohammadi",
            doctor_name="Dr. Rezaei",
            staff_name="Maryam",
            department_name="Cardiology",
            session_type="Visit",
            description="Checkup",
            medications=[{"name": "Aspirin", "dosage": "81mg"}],
            nursing_care=[{"type": "Injection"}],
            lab_tests=[{"name": "Blood Test"}],
            total_amount=200000.0,
            payment_status="Paid"
        )

    def test_save_medical_record(self):
        status, message = MedicalRecordController.save(
            unit_no=self.test_record.unit_no,
            full_name=self.test_record.full_name,
            doctor_name=self.test_record.doctor_name,
            staff_name=self.test_record.staff_name,
            department_name=self.test_record.department_name,
            session_type=self.test_record.session_type,
            description=self.test_record.description,
            medications=self.test_record.medications,
            nursing_care=self.test_record.nursing_care,
            lab_tests=self.test_record.lab_tests,
            total_amount=self.test_record.total_amount,
            payment_status=self.test_record.payment_status
        )
        self.assertTrue(status)
        self.assertEqual(message, "Medical Record Saved Successfully")
        self.logger.info("Tested save_medical_record")

    def test_update_medical_record_doctor_name(self):
        # Test individual field: doctor_name
        status, message = MedicalRecordController.update(
            unit_no=1001,
            doctor_name="Updated Dr.",  # Individual field
            # ... other fields same
        )
        self.assertTrue(status)
        self.logger.info("Tested update_medical_record_doctor_name")

    def test_update_medical_record_total_amount(self):
        # Test individual field: total_amount
        status, message = MedicalRecordController.update(
            unit_no=1001,
            total_amount=250000.0,  # Individual field
            # ... other fields same
        )
        self.assertTrue(status)
        self.logger.info("Tested update_medical_record_total_amount")

    def test_delete_medical_record(self):
        status, message = MedicalRecordController.delete(1001)
        self.assertTrue(status)
        self.assertEqual(message, "Medical Record Deleted Successfully")
        self.logger.info("Tested delete_medical_record")

    def test_find_all_medical_records(self):
        records = MedicalRecordController.find_all()
        self.assertIsInstance(records, list)
        self.logger.info("Tested find_all_medical_records")

    def test_find_by_unit_no_medical_record(self):
        status, record = MedicalRecordController.find_by_unit_no(1001)
        self.assertTrue(status)
        self.assertIsInstance(record, MedicalRecord)
        self.logger.info("Tested find_by_unit_no_medical_record")

if __name__ == '__main__':
    unittest.main()
