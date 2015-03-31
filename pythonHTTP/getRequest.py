__author__ = 'paroksh.saxena'

import requests

r = requests.get('https://github.com/timeline.json')

#status Cod
print(r.status_code)

#text of response
print(r.text)