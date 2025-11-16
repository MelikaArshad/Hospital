import unittest
from model.department import Department
from controller.department_controller import DepartmentController
from tools.logger import Logger

class TestDepartmentController(unittest.TestCase):
    def setUp(self):
        self.logger = Logger()
        self.test_dept = Department(
            department_id=1,
            department_name="Cardiology",
            department_controller="Dr. Rezaei"
        )

    def test_save_department(self):
        status, message = DepartmentController.save(
            department_name=self.test_dept.department_name,
            department_controller=self.test_dept.department_controller
        )
        self.assertTrue(status)
        self.assertEqual(message, "Department Saved Successfully")
        self.logger.info("Tested save_department")

    def test_update_department_name(self):
        # Test individual field: department_name
        status, message = DepartmentController.update(
            department_id=1,
            department_name="Updated Cardiology",  # Individual field
            department_controller=self.test_dept.department_controller
        )
        self.assertTrue(status)
        self.logger.info("Tested update_department_name")

    def test_update_department_controller(self):
        # Test individual field: department_controller
        status, message = DepartmentController.update(
            department_id=1,
            department_name=self.test_dept.department_name,
            department_controller="Updated Dr."  # Individual field
        )
        self.assertTrue(status)
        self.logger.info("Tested update_department_controller")

    def test_delete_department(self):
        status, message = DepartmentController.delete(1)
        self.assertTrue(status)
        self.assertEqual(message, "Department Deleted Successfully")
        self.logger.info("Tested delete_department")

    def test_find_all_departments(self):
        depts = DepartmentController.find_all()
        self.assertIsInstance(depts, list)
        self.logger.info("Tested find_all_departments")

    def test_find_by_id_department(self):
        status, dept = DepartmentController.find_by_id(1)
        self.assertTrue(status)
        self.assertIsInstance(dept, Department)
        self.logger.info("Tested find_by_id_department")

    def test_find_by_name_department(self):
        depts = DepartmentController.find_by_name("Cardiology")
        self.assertIsInstance(depts, list)
        self.logger.info("Tested find_by_name_department")

if __name__ == '__main__':
    unittest.main()
