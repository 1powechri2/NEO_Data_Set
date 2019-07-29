from datetime import datetime, timedelta

class DateGetter:

    def __init__(self):
        self.start_date = datetime(2018, 1, 1)
        self.end_date   = self.start_date

    def start_date_to_string(self):
        return self.start_date.strftime('%Y-%m-%d')

    def end_date_to_string(self):
        return self.end_date.strftime('%Y-%m-%d')

    def advance_date(self):
        self.start_date = self.end_date + timedelta(1)
        self.end_date   = self.start_date
