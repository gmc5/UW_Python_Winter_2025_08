import tempfile
import unittest
import json
from processing_classes import FileProcessor
from test_data_classes import Employee

class TestFileProcessor(unittest.TestCase):
    """
    This unit test class, TestFileProcessor, verifies the functionality of
    reading and writing employee data to a JSON file using FileProcessor,
    ensuring correct serialization and deserialization of Employee objects.
    """
    def setUp(self):
        """
        Creates a temporary file, stores its name, and
        closes it to prevent conflicts when writing data in tests.
        :return:
        """
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file_name = self.temp_file.name
        self.temp_file.close()  # Ensure file can be written

    def tearDown(self):
        """
        Deletes the temporary file after each test to ensure a clean testing
        environment.
        :return:
        """
        import os
        os.remove(self.temp_file_name)  # Clean up after test

    def test_read_data_from_file(self):
        """
        verifies that FileProcessor.read_employee_data_from_file() correctly
        reads employee data from a JSON file and maps it to Employee objects
        with expected attributes.
        :return:
        """
        sample_data = [
            {
                "FirstName": "Bob",
                "LastName": "Smith",
                "ReviewDate": "2025-03-16",
                "ReviewRating": 5
            },
            {
                "FirstName": "Vic",
                "LastName": "Vu",
                "ReviewDate": "2025-03-15",
                "ReviewRating": 3
            }
        ]
        # Write sample data to temp file
        with open(self.temp_file_name, "w") as file:
            json.dump(sample_data, file)

        # Read from temp file
        employees = [] #initialize empty list
        employees = FileProcessor.read_employee_data_from_file(self.temp_file_name, employees, Employee) #pass employee list, and Employee type

        # Validate first employee
        self.assertEqual(sample_data[0]["FirstName"], employees[0].first_name)
        self.assertEqual(sample_data[0]["LastName"], employees[0].last_name)
        self.assertEqual(sample_data[0]["ReviewDate"], employees[0].review_date)
        self.assertEqual(sample_data[0]["ReviewRating"], employees[0].review_rating)

        # Validate second employee
        self.assertEqual(sample_data[1]["FirstName"], employees[1].first_name)
        self.assertEqual(sample_data[1]["LastName"], employees[1].last_name)
        self.assertEqual(sample_data[1]["ReviewDate"], employees[1].review_date)
        self.assertEqual(sample_data[1]["ReviewRating"], employees[1].review_rating)

    def test_write_data_to_file(self):
        """
        verifies that employee data is correctly written to a file and then
        reads it back, ensuring the content matches the expected data.
        :return:
        """
        sample_data=[
            Employee("Vic", "Vu", "2025-03-16", 4),
            Employee("Bob","Smith","2025-03-16",5)
        ]
        FileProcessor.write_employee_data_to_file(self.temp_file_name,sample_data)

        with open(self.temp_file_name,"r") as file:
            file_data=json.load(file)

        self.assertEqual(len(sample_data),len(file_data))

        # Validate all employees
        for i in range(len(sample_data)):
            self.assertEqual(sample_data[i].first_name, file_data[i]["FirstName"])
            self.assertEqual(sample_data[i].last_name, file_data[i]["LastName"])
            self.assertEqual(sample_data[i].review_date, file_data[i]["ReviewDate"])
            self.assertEqual(sample_data[i].review_rating, file_data[i]["ReviewRating"])

if __name__ == "__main__":
    unittest.main()