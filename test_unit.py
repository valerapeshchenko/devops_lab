import gather
import unittest


class SysPython(unittest.TestCase):
    def setUp(self):
        '''Init'''

    def test_json_function(self):
        self.assertFalse(gather.json_file())

    def test_yaml_function(self):
        self.assertFalse(gather.yaml_file())

    def tearDown(self):
        '''Finish'''
