import urllib.request as req
import json
from api_key import key

# final_url = url + start_date + '&' + end_date + '&' + api_key
#
# neo = req.urlopen(final_url)
#
# req_data = neo.read()
#
# encoding = neo.info().get_content_charset('utf8')

class NeoGetter:

    def __init__(self, start_date, end_date):
        self.url = 'https://api.nasa.gov/neo/rest/v1/feed?'
        self.start_date = start_date
        self.end_date   = end_date
        self.api_key    = 'api_key=' + key

    def final_url():
        url + start_date + '&' + end_date + '&' + api_key

    def string():
        return json.loads(req_data.decode(encoding))

print(type(NeoGetter('start_date=2015-09-07', 'end_date=2015-09-08')))
