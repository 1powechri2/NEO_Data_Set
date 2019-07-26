import unittest
import csv_loader
import date_getter.date_getter as date_getter
import neo_getter.neo_getter as neo_getter

class CSVLoaderTest(unittest.TestCase):

    loader = csv_loader.CSVLoader()

    def test_it_initializes(self):
        self.assertIsInstance(self.loader, csv_loader.CSVLoader)



if __name__ == '__main__':
    unittest.main()
