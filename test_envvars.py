import os
import unittest

class TestEnvironmentVariable(unittest.TestCase):
    def test_modify_env_var(self):
        os.environ['TEST_VAR'] = '123'
        self.assertEqual(os.getenv('TEST_VAR'), '123')

if __name__ == '__main__':
    unittest.main()