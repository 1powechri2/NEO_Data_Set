import unittest
import date_getter as dates
from datetime import datetime

class TestNeoGetter(unittest.TestCase):

    getter = dates.DateGetter()

    def test_it_initializes(self):
        self.assertEqual(self.getter.start_date, datetime(2019, 1, 1, 0, 0))
        self.assertEqual(self.getter.end_date, datetime(2019, 1, 2, 0, 0))

    def test_start_date_to_string(self):
        self.assertEqual(self.getter.start_date_to_string(), '2019-01-01')

    def test_end_date_to_string(self):
        self.assertEqual(self.getter.end_date_to_string(), '2019-01-02')

    def test_advance_date(self):
        getter = dates.DateGetter()
        getter.advance_date()
        self.assertEqual(getter.start_date, datetime(2019, 1, 2, 0, 0))
        self.assertEqual(getter.end_date, datetime(2019, 1, 3, 0, 0))

if __name__ == '__main__':
    unittest.main()
