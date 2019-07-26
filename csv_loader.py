import date_getter.date_getter as date_getter
import neo_getter.neo_getter as neo_getter

class CSVLoader:

    def __init__(self):
        self.date_getter = date_getter.DateGetter()
        self.neo_getter = neo_getter.NeoGetter(self.date_getter.start_date, self.date_getter.end_date)
