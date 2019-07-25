import unittest
import neo_getter as neos

class TestNeoGetter(unittest.TestCase):

    def test_it_gets_neos(self):
        self.assertIsInstance(neos.get_neos(), dict)

if __name__ == '__main__':
    unittest.main()
