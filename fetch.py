import requests
import os

params = {'api_key' : 'tYY9bPjanRLE',}
r = requests.get('https://www.parsehub.com/api/v2/projects/tU2tHvFCqEBs/last_ready_run/data', params=params)

with open('/tmp/menus.tmp.json', 'w') as f:
        f.write(r.text)
os.rename('/tmp/menus.tmp.json', '/tmp/menus.json')
