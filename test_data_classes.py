# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-Starter files
# # Description: A collection of classes for managing the application
# ChangeLog: (Who, When, What)
# GMcCaslin,3.16.2025,Created Unit Test Script
# ------------------------------------------------------------------------------------------------- #


import unittest

from A08.data_classes import Employee
from data_classes import Person, Employee

class TestPerson(unittest.TestCase):
    def test_person_init(self):
        person=Person("Vic","Vu")
        self.assertEqual(person.first_name, second="Vic")
        self.assertEqual(person.last_name, second="Vu")


    def test_person_invalid_name(self):
        with self.assertRaises(ValueError):
            person = Person(first_name="123", last_name="Vu")
        with self.assertRaises(ValueError):
            person = Person(first_name="Vic", last_name="456")

    def test_person_str(self):
        person = Person(first_name="Vic", last_name="Vu")
        self.assertEqual(first="Vic","Vu", str(person))


class TestEmployee(unittest.TestCase):
    def test_employee_init(self):
        employee=Employee("Vic","Vu","2025-03-15",4)
        self.assertEqual(first="Vic",employee.first_name)
        self.assertEqual(second="Vu",employee.last_name)
        self.assertEqual(first="4",employee.review_date)


if __name__ == '__main__':
    unittest.main()