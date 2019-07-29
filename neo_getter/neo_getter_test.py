import unittest
import neo_getter as neos
import http.client

class TestNeoGetter(unittest.TestCase):

    getter = neos.NeoGetter('2015-09-07', '2015-09-08')

    def test_it_initializes(self):
        self.assertEqual(self.getter.url, 'https://api.nasa.gov/neo/rest/v1/feed?')
        self.assertEqual(self.getter.start_date, '2015-09-07')
        self.assertEqual(self.getter.end_date, '2015-09-07')

    def test_it_gets_raw_neos(self):
        self.assertIsInstance(self.getter.neo(), http.client.HTTPResponse)

    def test_it_gets_neos(self):
        self.assertIsInstance(self.getter.neoData(), dict)
        self.assertEqual(self.getter.neoData()['element_count'], 10)

if __name__ == '__main__':
    unittest.main()
