# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-Starter files
# # Description: A collection of classes for managing the application
# ChangeLog: (Who, When, What)
# GMcCaslin,3.16.2025,Created Script
# ------------------------------------------------------------------------------------------------- #

import unittest
from unittest.mock import patch
from presentation_classes import IO

class TestIOProcessor(unittest.TestCase):
    """
    verifies the input_menu_choice method correctly returns the user's input by
    mocking the input function.
    """
    def test_input_menu_choice_returns_user_input(self):
        """Tests that input_menu_choice returns the user's input."""
        with patch(target="builtins.input", return_value="2"):
            choice = IO.input_menu_choice()
            self.assertEqual("2", choice)

if __name__ == "__main__":
    unittest.main()