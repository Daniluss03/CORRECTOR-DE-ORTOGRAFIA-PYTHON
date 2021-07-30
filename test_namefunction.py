import unittest
from function_names import get_names as ds

class NameTestCase(unittest.TestCase):
    """test for 'namefunction.py'"""
    def test_first_last_name(self):
        """do names like 'janis joplin'"""
        formatted_name=ds('janis','joplin')
        self.assertEqual(formatted_name,'janis joplin',)
unittest.main()
