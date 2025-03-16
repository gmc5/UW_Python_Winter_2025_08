import unittest

from data_classes import Person, Employee

class TestPerson(unittest.TestCase):
    """
    This unittest test case verifies the correct initialization,
    validation of names, and string representation of the Person class.
    """
    def test_person_init(self):
        person = Person("Vic", "Vu")
        self.assertEqual("Vic", person.first_name)
        self.assertEqual("Vu", person.last_name)

    def test_person_invalid_name(self):
        """
        Verifies that the Person class initializes correctly with the given
        first and last name.
        :return:
        """
        with self.assertRaises(ValueError):
            person = Person(first_name="123", last_name="Vu")
        with self.assertRaises(ValueError):
            person = Person(first_name="Vic", last_name="456")

    def test_person_str(self):
        """
        verifies that a Person object correctly stores and returns the
        first_name and last_name attributes.
        :return:
        """
        person = Person(first_name="Vic", last_name="Vu")
        self.assertEqual(person.first_name, "Vic")
        self.assertEqual(person.last_name, "Vu")

class TestEmployee(unittest.TestCase):
    """
    Verifies the correct initialization of the Employee class and ensures that
    an out-of-range review rating raises a ValueError.
    """
    def test_employee_init(self):
        """
        verifies that the Employee class initializes attributes correctly with
        given values.
        :return:
        """
        employee = Employee("Vic", "Vu", "2025-03-15", 4)
        self.assertEqual("Vic", employee.first_name)
        self.assertEqual("Vu", employee.last_name)
        self.assertEqual("2025-03-15", employee.review_date)
        self.assertEqual(4, employee.review_rating)

    def test_employee_review_rating_out_of_range(self):
        """
        verifies that creating an Employee with a review rating of
        6 (out of the valid range) raises a ValueError.
        :return:
        """
        with self.assertRaises(ValueError):
            employee = Employee("Vic", "Vu", "2025-03-15", 6)

if __name__ == '__main__':
    unittest.main()