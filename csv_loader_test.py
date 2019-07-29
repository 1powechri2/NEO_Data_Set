import unittest
import csv_loader
import date_getter.date_getter as date_getter
import neo_getter.neo_getter as neo_getter

class CSVLoaderTest(unittest.TestCase):

    loader = csv_loader.CSVLoader()

    def test_it_initializes(self):
        self.assertIsInstance(self.loader, csv_loader.CSVLoader)

    def test_it_gets_neos_from_neo_getter(self):
        self.assertIsInstance(self.loader.get_neos_from_neo_getter(), dict)
        self.assertEqual(self.loader.get_neos_from_neo_getter()['element_count'], 11)

    def test_date_incrementer(self):
        self.assertEqual(self.loader.date_incrementer(), 365)



if __name__ == '__main__':
    unittest.main()
