import unittest
from index import UI


class TestUI(unittest.TestCase):
    
    def test_init_current_view_is_none(self):
        self.assertEqual(str(_current_view), "None") 
