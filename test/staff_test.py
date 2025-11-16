import unittest
from model.staff import Staff
from controller.staff_controller import StaffController
from tools.logger import Logger

class TestStaffController(unittest.TestCase):
    def setUp(self):
        self.logger = Logger()
        self.test_staff = Staff(
            staff_id=101,
            full_name="Ali Ahmadi",
            father_name="Hassan",
            national_code="1234567890",
            personal_id_no="S1001",
            degree="Bachelor",
            birth_date="1370/05/15",
            age=35,
            phone_number="09123456789",
            address="Tehran",
            username="ali_user",
            password="pass123",
            ward="Internal",
            role="Nurse"
        )

    def test_save_staff(self):
        status, message = StaffController.save(
            full_name=self.test_staff.full_name,
            father_name=self.test_staff.father_name,
            national_code=self.test_staff.national_code,
            personal_id_no=self.test_staff.personal_id_no,
            degree=self.test_staff.degree,
            birth_date=self.test_staff.birth_date,
            age=self.test_staff.age,
            phone_number=self.test_staff.phone_number,
            address=self.test_staff.address,
            username=self.test_staff.username,
            password=self.test_staff.password,
            ward=self.test_staff.ward,
            role=self.test_staff.role
        )
        self.assertTrue(status)
        self.assertEqual(message, "Staff Saved Successfully")
        self.logger.info("Tested save_staff")

    def test_update_staff_full_name(self):
        # Test individual field: full_name
        status, message = StaffController.update(
            staff_id=101,
            full_name="Updated Name",  # Individual field
            # ... other fields same
        )
        self.assertTrue(status)
        self.logger.info("Tested update_staff_full_name")

    def test_update_staff_age(self):
        # Test individual field: age
        status, message = StaffController.update(
            staff_id=101,
            age=40,  # Individual field
            # ... other fields same
        )
        self.assertTrue(status)
        self.logger.info("Tested update_staff_age")

    def test_delete_staff(self):
        status, message = StaffController.delete(101)
        self.assertTrue(status)
        self.assertEqual(message, "Staff Deleted Successfully")
        self.logger.info("Tested delete_staff")

    def test_find_all_staff(self):
        staff_list = StaffController.find_all()
        self.assertIsInstance(staff_list, list)
        self.logger.info("Tested find_all_staff")

    def test_find_by_id_staff(self):
        status, staff = StaffController.find_by_id(101)
        self.assertTrue(status)
        self.assertIsInstance(staff, Staff)
        self.logger.info("Tested find_by_id_staff")

    def test_find_by_name_staff(self):
        staff = StaffController.find_by_name("Ali")
        self.assertIsInstance(staff, list)
        self.logger.info("Tested find_by_name_staff")

if __name__ == '__main__':
    unittest.main()
