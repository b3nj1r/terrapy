import numpy as np
import polyline as pl
import requests


def gen_map(o,x,y,a):

    # obtain pair values
    xs = np.arange(o[0],o[0]+x,0.1*a)
    ys = np.arange(o[1],o[1]+y,0.1*a)

    # format pairs
    result = []
    for i in xs:
        for j in ys:
            result.append( (i,j) )
    # return google polyline format
    return(pl.encode(result))


# generate coordinate pairs
loc = gen_map([36,-94],5,5,5)

# request height data from opentopodata
params = {'locations':loc,'interpolation':'cubic'}
url = 'https://api.opentopodata.org/v1/ned10m'
r = requests.get(url,params=params)

# assign point map
pmap = r.json()['results']

# assign height values to coordinate pairs
x,y,z = [],[],[]
for p in pmap:
    x.append(p['location']['lat'])
    y.append(p["location"]['lng'])
    z.append(p['elevation'])

