import date_getter.date_getter as date_getter
import neo_getter.neo_getter as neo_getter
import csv
from datetime import datetime


class CSVLoader:

    def __init__(self):
        self.date_getter = date_getter.DateGetter()
        self.neo_getter = neo_getter.NeoGetter(self.date_getter.start_date_to_string(), self.date_getter.end_date_to_string())

    def get_neos_from_neo_getter(self):
        return self.neo_getter.neoData()

    def date_incrementer(self):
        count = 1
        while self.date_getter.start_date_to_string() != datetime(2018, 12, 31).strftime('%Y-%m-%d'):
            count += 1
            self.date_getter.advance_date();
            self.date_getter.start_date_to_string();
            self.date_getter.end_date_to_string();
        return count
