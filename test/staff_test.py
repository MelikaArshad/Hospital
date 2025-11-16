import unittest
from controller.staff_controller import StaffController
from tools.logger import Logger

class TestStaffController(unittest.TestCase):
    def setUp(self):
        self.logger = Logger()

    def test_save_staff(self):
        status, message = StaffController.save(
            full_name="Test Staff", father_name="Father", national_code="7777777777",
            personal_id_no="S9999", degree="Bachelor", birth_date="1370/01/01", age=35,
            phone_number="09123456789", address="Tehran", username="test_staff",
            password="pass123", ward="Internal", role="Nurse"
        )
        self.assertTrue(status)
        self.assertIn("Successfully", message)
        self.logger.info("Tested save_staff")

    def test_update_staff(self):
        status, message = StaffController.update(staff_id=101, full_name="Updated Staff")
        self.assertTrue(status)
        self.assertIn("Updated", message)
        self.logger.info("Tested update_staff")

    def test_update_nonexistent_staff(self):
        status, message = StaffController.update(staff_id=999999, full_name="Nonexistent")
        self.assertFalse(status)
        self.logger.info("Tested update_nonexistent_staff")

    def test_delete_staff(self):
        status, message = StaffController.delete(101)
        self.assertTrue(status)
        self.assertIn("Deleted", message)
        self.logger.info("Tested delete_staff")

    def test_find_all_staff(self):
        staff_list = StaffController.find_all()
        self.assertIsInstance(staff_list, list)
        self.logger.info("Tested find_all_staff")

    def test_find_by_id_staff(self):
        status, staff = StaffController.find_by_id(101)
        self.assertTrue(status)
        self.logger.info("Tested find_by_id_staff")

    def test_find_by_id_not_found(self):
        status, staff = StaffController.find_by_id(999999)
        self.assertFalse(status)
        self.logger.info("Tested find_by_id_not_found")

    def test_find_by_id_non_existent_staff(self):
        status, staff = StaffController.find_by_id(999999)
        self.assertFalse(status)
        self.logger.info("Tested find_by_id_non_existent_staff")

    def test_find_by_name_staff(self):
        staff_list = StaffController.find_by_name("Test")
        self.assertIsInstance(staff_list, list)
        self.logger.info("Tested find_by_name_staff")

if __name__ == '__main__':
    unittest.main()


