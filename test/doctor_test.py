import unittest
from controller.doctor_controller import DoctorController
from tools import Logger

class TestDoctorController(unittest.TestCase):
    def setUp(self):
        self.logger = Logger()

    def test_save_doctor(self):
        status, message = DoctorController.save(
            f"Test Doctor", "Cardiology", "Father",
            "8888888888", "D9999", "Specialist",
            "1360/01/01", 45, "09123456789", "Tehran",
            "test_dr", "pass123")
        self.assertTrue(status)
        self.assertIn("Successfully", message)
        self.logger.info("Tested save_doctor")

    def test_update_doctor(self):
        status, message = DoctorController.update(1, "Updated Doctor")
        self.assertTrue(status)
        self.assertIn("Updated", message)
        self.logger.info("Tested update_doctor")

    def test_update_nonexistent_doctor(self):
        status, message = DoctorController.update(999999, "Nonexistent")
        self.assertFalse(status)
        self.logger.info("Tested update_nonexistent_doctor")

    def test_delete_doctor(self):
        status, message = DoctorController.delete(1)
        self.assertTrue(status)
        self.assertIn("Deleted", message)
        self.logger.info("Tested delete_doctor")

    def test_find_all_doctors(self):
        doctors_list = DoctorController.find_all()
        self.assertIsInstance(doctors_list, list)
        self.logger.info("Tested find_all_doctors")

    def test_find_by_id_doctor(self):
        status, doctor = DoctorController.find_by_id(1)
        self.assertTrue(status)
        self.logger.info("Tested find_by_id_doctor")

    def test_find_by_id_not_found(self):
        status, doctor = DoctorController.find_by_id(999999)
        self.assertFalse(status)
        self.logger.info("Tested find_by_id_not_found")

    def test_find_by_id_non_existent_doctor(self):
        status, doctor = DoctorController.find_by_id(999999)
        self.assertFalse(status)
        self.logger.info("Tested find_by_id_non_existent_doctor")

    def test_find_by_name_doctor(self):
        doctors_list = DoctorController.find_by_name("Test")
        self.assertIsInstance(doctors_list, list)
        self.logger.info("Tested find_by_name_doctor")

if __name__ == '__main__':
    unittest.main()

