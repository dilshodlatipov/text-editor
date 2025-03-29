import unittest
import os
from main import create_file, read_file, delete_file


class TestFileOperations(unittest.TestCase):
    def setUp(self):
        """Set up test environment."""
        self.test_filename = "test_file.txt"
        self.test_content = "Hello, this is a test file!"

    def tearDown(self):
        """Clean up after tests."""
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_create_file(self):
        """Test file creation."""
        create_file(self.test_filename, self.test_content)
        self.assertTrue(os.path.exists(self.test_filename))

    def test_read_file(self):
        """Test reading a file."""
        create_file(self.test_filename, self.test_content)
        with open(self.test_filename, 'r') as file:
            content = file.read()
        self.assertEqual(content, self.test_content)

    def test_delete_file(self):
        """Test deleting a file."""
        create_file(self.test_filename, self.test_content)
        delete_file(self.test_filename)
        self.assertFalse(os.path.exists(self.test_filename))


if __name__ == "__main__":
    unittest.main()
