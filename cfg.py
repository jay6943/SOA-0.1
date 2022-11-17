work = '../mask/SOA-0.1/'
libs = '../mask/SOA-0.1/lib/'

data = []

angle = 7

wg = 2
wt = 0.8
ch = 250

ltpr = 5
wtpr = 2

size = 10000
mask = 10900
area = [[1, 0], [-1, 0], [0, 0], [-1, -1], [0, -1]]

layer = {} # 2 for (0, 0) mask position
layer['core'] = 2
layer['edge'] = 2
layer['slab'] = 2
layer['sio2'] = 2
layer['fill'] = 2
layer['gold'] = 2
layer['keys'] = 2
layer['bars'] = 2
layer['hole'] = 2
layer['recs'] = 2
layer['tops'] = 2
layer['cuts'] = 2
layer['text'] = 2