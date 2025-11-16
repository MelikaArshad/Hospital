import unittest
from model.patient import Patient
from controller.patient_controller import PatientController
from tools.logger import Logger

class TestPatientController(unittest.TestCase):
    def setUp(self):
        self.logger = Logger()
        self.test_patient = Patient(
            unit_no=1001,
            full_name="Ahmad Mohammadi",
            father_name="Mohammad",
            national_code="1234567890",
            birth_date="1370/05/15",
            phone_number="09123456789",
            age=30,
            height=175,
            weight=70,
            attending_physician="Dr. Rezaei",
            kind_of_ad="Inpatient",
            date_of_admission="1404/08/15",
            ward="Cardiology",
            room="205",
            bed="3",
            notes_text="No notes"
        )

    def test_save_patient(self):
        status, message = PatientController.save(
            full_name=self.test_patient.full_name,
            father_name=self.test_patient.father_name,
            national_code=self.test_patient.national_code,
            birth_date=self.test_patient.birth_date,
            phone_number=self.test_patient.phone_number,
            age=self.test_patient.age,
            height=self.test_patient.height,
            weight=self.test_patient.weight,
            attending_physician=self.test_patient.attending_physician,
            kind_of_ad=self.test_patient.kind_of_ad,
            date_of_admission=self.test_patient.date_of_admission,
            ward=self.test_patient.ward,
            room=self.test_patient.room,
            bed=self.test_patient.bed,
            notes_text=self.test_patient.notes_text
        )
        self.assertTrue(status)
        self.assertEqual(message, "Patient Saved Successfully")
        self.logger.info("Tested save_patient")

    def test_update_patient_full_name(self):
        # Test individual field: full_name
        status, message = PatientController.update(
            unit_no=1001,
            full_name="Updated Name",  # Individual field update
            father_name=self.test_patient.father_name,
            # ... other fields same as test_patient
        )
        self.assertTrue(status)
        self.assertEqual(message, "Patient Updated Successfully")
        self.logger.info("Tested update_patient_full_name")

    def test_update_patient_age(self):
        # Test individual field: age
        status, message = PatientController.update(
            unit_no=1001,
            age=35,  # Individual field update
            # ... other fields same
        )
        self.assertTrue(status)
        self.logger.info("Tested update_patient_age")

    def test_delete_patient(self):
        status, message = PatientController.delete(1001)
        self.assertTrue(status)
        self.assertEqual(message, "Patient Deleted Successfully")
        self.logger.info("Tested delete_patient")

    def test_find_all_patients(self):
        patients_list = PatientController.find_all()
        self.assertIsInstance(patients_list, list)
        self.logger.info("Tested find_all_patients")

    def test_find_by_id_patient(self):
        status, patient = PatientController.find_by_id(1001)
        self.assertTrue(status)
        self.assertIsInstance(patient, Patient)
        self.logger.info("Tested find_by_id_patient")

    def test_find_by_name_patient(self):
        patients = PatientController.find_by_name("Ahmad")
        self.assertIsInstance(patients, list)
        self.logger.info("Tested find_by_name_patient")

if __name__ == '__main__':
    unittest.main()
