# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-Starter files
# # Description: A collection of classes for managing the application
# ChangeLog: (Who, When, What)
# GMcCaslin,3.16.2025,Created Script
# ------------------------------------------------------------------------------------------------- #


from datetime import date


# Data -------------------------------------------- #
FILE_NAME: str = 'EmployeeRatings.json'



class Person:
    """
    A class representing person data.

    Properties:
    - first_name (str): The person's first name.
    - last_name (str): The person's last name.

    ChangeLog:
    - GMcCaslin, 3.15.2025: Created the class.
    """

    def __init__(self, first_name: str = "", last_name: str = ""):
        self.first_name = first_name
        self.last_name = last_name
        """
        Defines the __init__ method of a class, initializing two optional 
        instance variables, first_name and last_name, with default empty 
        string values.
        """

    @property
    def first_name(self):
        return self.__first_name.title()
    """
     Defines a property method first_name that returns the value of the private 
     attribute __first_name with its first letter capitalized using the title() 
     method.
    """

    @first_name.setter
    def first_name(self, value: str):
        if value.isalpha() or value == "":
            self.__first_name = value
        else:
            raise ValueError("The first name should not contain numbers.")
        """
        Defines a setter method for the first_name attribute, which ensures that 
        the value assigned is either alphabetic or an empty string, raising a 
        ValueError if the value contains numbers.
        """

    @property
    def last_name(self):
        return self.__last_name.title()
    """
    Defines a property method last_name that returns the value of the private 
    attribute __last_name with its first letter capitalized.
    """

    @last_name.setter
    def last_name(self, value: str):
        if value.isalpha() or value == "":
            self.__last_name = value
        else:
            raise ValueError("The last name should not contain numbers.")
        """
        Defines a setter method for the last_name attribute, ensuring 
        that the value assigned is either a string of alphabetic characters or 
        an empty string, raising a ValueError if the value contains numbers.
        """

    def __str__(self):
        return f"{self.first_name},{self.last_name}"
    """
    Defines a __str__ method that returns a string representation of an object, 
    formatting it as the first name followed by the last name, separated by a comma.
    """


class Employee(Person):
    """
    A class representing employee data.

    Properties:
    - first_name (str): The employee's first name.
    - last_name (str): The employee's last name.
    - review_date (date): The data of the employee review.
    - review_rating (int): The review rating of the employee's performance (1-5)

    ChangeLog:
    - GMcCaslin, 3.15.2025: Created the class.
    """

    def __init__(self, first_name: str = "", last_name: str = "", review_date: str = "1900-01-01", review_rating: int = 3):

        super().__init__(first_name=first_name,last_name=last_name)
        self.review_date = review_date
        self.review_rating = review_rating
        """
        Defines an __init__ method for a class that inherits from a parent class, 
        initializing the first_name, last_name, review_date, and review_rating 
        attributes, with default values for the latter two.
        """

    @property
    def review_date(self):
        return self.__review_date
    """
    Defines a property method review_date that returns the value of the private 
    attribute __review_date.
    """

    @review_date.setter
    def review_date(self, value: str):
        try:
            date.fromisoformat(value)
            self.__review_date = value
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        """
        Defines a setter method for the review_date attribute, ensuring that the 
        input value is in the correct YYYY-MM-DD date format before assigning it 
        to the private attribute __review_date, and raises a ValueError if the 
        format is incorrect.
        """

    @property
    def review_rating(self):
        return self.__review_rating
    """
    Defines a property method review_rating that allows access to the private 
    attribute __review_rating while encapsulating it and ensuring controlled access.
    """

    @review_rating.setter
    def review_rating(self, value: int):
        if value in (1, 2, 3, 4, 5):
            self.__review_rating = value
        else:
            raise ValueError("Please choose only values 1 through 5")
        """
         Defines a setter method for the review_rating attribute, ensuring that 
         the value assigned is between 1 and 5; otherwise, it raises a ValueError.
        """

    def __str__(self):
        return f"{self.first_name},{self.last_name},{self.review_date},{self.__review_rating}"
    """
    Returns a formatted string representation of an object, displaying the first name, 
    last name, review date, and review rating.
    """
