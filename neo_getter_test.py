import unittest
import neo_getter as neos

class TestNeoGetter(unittest.TestCase):

    def test_it_gets_neos(self):
        self.assertIsInstance(neos.NeoGetter('start_date=2015-09-07', 'end_date=2015-09-08'), neos.NeoGetter)

if __name__ == '__main__':
    unittest.main()
