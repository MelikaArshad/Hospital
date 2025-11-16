import unittest
from model.doctor import Doctor
from controller.doctor_controller import DoctorController
from tools.logger import Logger

class TestDoctorController(unittest.TestCase):
    def setUp(self):
        self.logger = Logger()
        self.test_doctor = Doctor(
            doctor_id=1,
            full_name="Dr. Rezaei",
            department_controller="Cardiology",
            father_name="Hassan",
            national_code="0987654321",
            personal_id_no="D1001",
            degree="Specialist",
            birth_date="1360/01/01",
            age=45,
            phone_number="09123456789",
            address="Tehran",
            username="dr_rezaei",
            password="pass123"
        )

    def test_save_doctor(self):
        status, message = DoctorController.save(
            full_name=self.test_doctor.full_name,
            department_controller=self.test_doctor.department_controller,
            father_name=self.test_doctor.father_name,
            national_code=self.test_doctor.national_code,
            personal_id_no=self.test_doctor.personal_id_no,
            degree=self.test_doctor.degree,
            birth_date=self.test_doctor.birth_date,
            age=self.test_doctor.age,
            phone_number=self.test_doctor.phone_number,
            address=self.test_doctor.address,
            username=self.test_doctor.username,
            password=self.test_doctor.password
        )
        self.assertTrue(status)
        self.assertEqual(message, "Doctor Saved Successfully")
        self.logger.info("Tested save_doctor")

    def test_update_doctor_full_name(self):
        # Test individual field: full_name
        status, message = DoctorController.update(
            doctor_id=1,
            full_name="Updated Dr. Name",  # Individual field
            # ... other fields same
        )
        self.assertTrue(status)
        self.logger.info("Tested update_doctor_full_name")

    def test_update_doctor_age(self):
        # Test individual field: age
        status, message = DoctorController.update(
            doctor_id=1,
            age=50,  # Individual field
            # ... other fields same
        )
        self.assertTrue(status)
        self.logger.info("Tested update_doctor_age")

    def test_delete_doctor(self):
        status, message = DoctorController.delete(1)
        self.assertTrue(status)
        self.assertEqual(message, "Doctor Deleted Successfully")
        self.logger.info("Tested delete_doctor")

    def test_find_all_doctors(self):
        doctors_list = DoctorController.find_all()
        self.assertIsInstance(doctors_list, list)
        self.logger.info("Tested find_all_doctors")

    def test_find_by_id_doctor(self):
        status, doctor = DoctorController.find_by_id(1)
        self.assertTrue(status)
        self.assertIsInstance(doctor, Doctor)
        self.logger.info("Tested find_by_id_doctor")

    def test_find_by_name_doctor(self):
        doctors = DoctorController.find_by_name("Rezaei")
        self.assertIsInstance(doctors, list)
        self.logger.info("Tested find_by_name_doctor")

if __name__ == '__main__':
    unittest.main()
