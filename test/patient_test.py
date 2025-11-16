import unittest
from controller.patient_controller import PatientController
from tools.logger import Logger

class TestPatientController(unittest.TestCase):
    def setUp(self):
        self.logger = Logger()

    def test_save_patient(self):
        status, message = PatientController.save(
            full_name="Test Patient", father_name="Father", national_code="9999999999",
            birth_date="1370/01/01", phone_number="09123456789", age=30, height=175, weight=70,
            attending_physician="Dr. Test", kind_of_ad="Inpatient", date_of_admission="1404/01/01",
            ward="Cardiology", room="101", bed="1", notes_text="Test"
        )
        self.assertTrue(status)
        self.assertIn("Successfully", message)
        self.logger.info("Tested save_patient")

    def test_update_patient(self):
        status, message = PatientController.update(unit_no=1001, full_name="Updated Patient")
        self.assertTrue(status)
        self.assertIn("Updated", message)
        self.logger.info("Tested update_patient")

    def test_update_nonexistent_patient(self):
        status, message = PatientController.update(unit_no=999999, full_name="Nonexistent")
        self.assertFalse(status)
        self.logger.info("Tested update_nonexistent_patient")

    def test_delete_patient(self):
        status, message = PatientController.delete(1001)
        self.assertTrue(status)
        self.assertIn("Deleted", message)
        self.logger.info("Tested delete_patient")

    def test_find_all_patients(self):
        patients_list = PatientController.find_all()
        self.assertIsInstance(patients_list, list)
        self.logger.info("Tested find_all_patients")

    def test_find_by_id_patient(self):
        status, patient = PatientController.find_by_id(1001)
        self.assertTrue(status)
        self.logger.info("Tested find_by_id_patient")

    def test_find_by_id_not_found(self):
        status, patient = PatientController.find_by_id(999999)
        self.assertFalse(status)
        self.logger.info("Tested find_by_id_not_found")

    def test_find_by_id_non_existent_patient(self):
        status, patient = PatientController.find_by_id(999999)
        self.assertFalse(status)
        self.logger.info("Tested find_by_id_non_existent_patient")

    def test_find_by_name_patient(self):
        patients_list = PatientController.find_by_name("Test")
        self.assertIsInstance(patients_list, list)
        self.logger.info("Tested find_by_name_patient")

if __name__ == '__main__':
    unittest.main()



