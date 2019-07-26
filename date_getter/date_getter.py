from datetime import datetime, timedelta

class DateGetter:

    def __init__(self):
        self.start_date = datetime(2019, 1, 1)
        self.end_date   = self.start_date + timedelta(1)

    def start_date_to_string(self):
        return self.start_date.strftime('%Y-%m-%d')

    def end_date_to_string(self):
        return self.end_date.strftime('%Y-%m-%d')

    def advance_date(self):
        self.start_date = self.end_date
        self.end_date   = self.start_date + timedelta(1)
