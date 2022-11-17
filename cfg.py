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
layer['active'] = 2
layer['metal'] = 2
layer['p-open'] = 2
layer['unknown'] = 2