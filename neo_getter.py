import urllib.request as req
import json
from api_key import key

url = 'https://api.nasa.gov/neo/rest/v1/feed?'

start_date = 'start_date=2015-09-07'

end_date = 'end_date=2015-09-08'

api_key = 'api_key=' + key

final_url = url + start_date + '&' + end_date + '&' + api_key

neo = req.urlopen(final_url)

req_data = neo.read()

encoding = neo.info().get_content_charset('utf8')

def string():
    return json.loads(req_data.decode(encoding))
