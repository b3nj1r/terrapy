#request and format data
import matplotlib.pyplot as plt
import numpy as np
import requests

# request height data from opentopodata
loc= '32,-97 | 32.1, -97 | 32.2, -97 | 32.3, -97 | 32.4, -97 | 32.5, -97 | 32.6, -97 | 32.7, -97 | 32.8, -97 | 32.9, -97 | 33, -97'
params = {'locations':loc,'interpolation':'cubic'}
url = 'https://api.opentopodata.org/v1/ned10m'
r = requests.get(url,params=params)

# assign point map
pmap = r.json()['results']

# assign height values to coordinate pairs
ps = []
for p in pmap:
    ps.append([p['location']['lat'],p["location"]['lng'],p['elevation']])

print(ps)
