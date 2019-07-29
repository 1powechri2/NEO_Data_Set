import date_getter.date_getter as date_getter
import neo_getter.neo_getter as neo_getter
import csv
from datetime import datetime
import pprint

class CSVLoader:

    def __init__(self):
        self.date_getter = date_getter.DateGetter()
        self.neo_getter = neo_getter.NeoGetter(self.date_getter.start_date_to_string(), self.date_getter.end_date_to_string())

    def get_neos_from_neo_getter(self):
        return self.neo_getter.neoData()

    def date_incrementer(self):
        while self.neo_getter.end_date != '2018-12-31':
            self.date_getter.advance_date();
            self.neo_getter.start_date = self.date_getter.start_date_to_string();
            self.neo_getter.end_date   = self.date_getter.end_date_to_string();
            data = self.get_neos_from_neo_getter();
            self.data_to_csv(data);

    def write_headers(self):
        with open('neos_from_2018.csv', mode='w') as csv_file:
            fieldnames = ['absolute_magnitude_h', 'close_approach_date',
                         'miss_distance_astronomical', 'miss_distance_lunar',
                         'miss_distance_kilometers', 'miss_distance_miles',
                         'relative_velocity_kph', 'relative_velocity_kps',
                         'relative_velocity_mph', 'estimated_max_diameter_kilometers',
                         'estimated_min_diameter_kilometers', 'estimated_max_diameter_miles',
                         'estimated_min_diameter_miles', 'id', 'is_potentially_hazardous',
                         'is_sentry_object', 'name']
            writer     = csv.DictWriter(csv_file, fieldnames = fieldnames)
            writer.writeheader()

    def data_to_csv(self, data):
        neos = data['near_earth_objects'][self.neo_getter.end_date];
        for row in neos:
            with open('neos_from_2018.csv', mode='a') as csv_file:
                fieldnames = ['absolute_magnitude_h', 'close_approach_date',
                             'miss_distance_astronomical', 'miss_distance_lunar',
                             'miss_distance_kilometers', 'miss_distance_miles',
                             'relative_velocity_kph', 'relative_velocity_kps',
                             'relative_velocity_mph', 'estimated_max_diameter_kilometers',
                             'estimated_min_diameter_kilometers', 'estimated_max_diameter_miles',
                             'estimated_min_diameter_miles', 'id', 'is_potentially_hazardous',
                             'is_sentry_object', 'name']

                writer = csv.DictWriter(csv_file, fieldnames = fieldnames);
                writer.writerow({'absolute_magnitude_h': row['absolute_magnitude_h'],
                                 'close_approach_date': row['close_approach_data'][0]['close_approach_date'],
                                 'miss_distance_astronomical': row['close_approach_data'][0]['miss_distance']['astronomical'],
                                 'miss_distance_lunar': row['close_approach_data'][0]['miss_distance']['lunar'],
                                 'miss_distance_kilometers': row['close_approach_data'][0]['miss_distance']['kilometers'],
                                 'miss_distance_miles': row['close_approach_data'][0]['miss_distance']['miles'],
                                 'relative_velocity_kph': row['close_approach_data'][0]['relative_velocity']['kilometers_per_hour'],
                                 'relative_velocity_kps': row['close_approach_data'][0]['relative_velocity']['kilometers_per_second'],
                                 'relative_velocity_mph': row['close_approach_data'][0]['relative_velocity']['miles_per_hour'],
                                 'estimated_max_diameter_kilometers': row['estimated_diameter']['kilometers']['estimated_diameter_max'],
                                 'estimated_min_diameter_kilometers': row['estimated_diameter']['kilometers']['estimated_diameter_min'],
                                 'estimated_max_diameter_miles': row['estimated_diameter']['miles']['estimated_diameter_max'],
                                 'estimated_min_diameter_miles': row['estimated_diameter']['miles']['estimated_diameter_min'],
                                 'id': row['id'],
                                 'is_potentially_hazardous': row['is_potentially_hazardous_asteroid'],
                                 'is_sentry_object': row['is_sentry_object'],
                                 'name': row['name']
                                 })

x = CSVLoader()

x.write_headers()
x.date_incrementer()
