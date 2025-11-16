import unittest
from controller import DepartmentController
from tools import Logger

class TestDepartmentController(unittest.TestCase):
    def setUp(self):
        self.logger = Logger()

    def test_save_department(self):
        status, message = DepartmentController.save("Test Department", "Test Controller")
        self.assertTrue(status)
        self.assertIn("Successfully", message)
        self.logger.info("Tested save_department")

    def test_update_department(self):
        status, message = DepartmentController.update(1, "Updated Dept")
        self.assertTrue(status)
        self.assertIn("Updated", message)
        self.logger.info("Tested update_department")

    def test_update_nonexistent_department(self):
        status, message = DepartmentController.update(999999, "Nonexistent")
        self.assertFalse(status)
        self.logger.info("Tested update_nonexistent_department")

    def test_delete_department(self):
        status, message = DepartmentController.delete(1)
        self.assertTrue(status)
        self.assertIn("Deleted", message)
        self.logger.info("Tested delete_department")

    def test_find_all_departments(self):
        depts = DepartmentController.find_all()
        self.assertIsInstance(depts, list)
        self.logger.info("Tested find_all_departments")

    def test_find_by_id_department(self):
        status, dept = DepartmentController.find_by_id(1)
        self.assertTrue(status)
        self.logger.info("Tested find_by_id_department")

    def test_find_by_id_not_found(self):
        status, dept = DepartmentController.find_by_id(999999)
        self.assertFalse(status)
        self.logger.info("Tested find_by_id_not_found")

    def test_find_by_id_non_existent_department(self):
        status, dept = DepartmentController.find_by_id(999999)
        self.assertFalse(status)
        self.logger.info("Tested find_by_id_non_existent_department")

    def test_find_by_name_department(self):
        depts = DepartmentController.find_by_name("Test")
        self.assertIsInstance(depts, list)
        self.logger.info("Tested find_by_name_department")

if __name__ == '__main__':
    unittest.main()

