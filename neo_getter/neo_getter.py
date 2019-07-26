import urllib.request as req
import json
from api_key import key

class NeoGetter:
    def __init__(self, start_date, end_date):
        self.url = 'https://api.nasa.gov/neo/rest/v1/feed?'
        self.start_date = start_date
        self.end_date   = end_date
        self.api_key    = 'api_key=' + key

    def final_url(self):
        return self.url + 'start_date=' + self.start_date + '&end_date=' + self.end_date + '&' + self.api_key

    def neo(self):
        return req.urlopen(self.final_url())

    def req_data(self):
        return self.neo().read()

    def encoding(self):
        return self.neo().info().get_content_charset('utf8')

    def neoData(self):
        return json.loads(self.req_data().decode(self.encoding()))
