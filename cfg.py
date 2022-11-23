work = '../mask/SOA-0.1/'
libs = '../mask/SOA-0.1/lib/'

data = []

tilt = -7

wg = 2
wt = 0.8
ch = 250

ltpr = 5
wtpr = 2

size = 10000
mask = 10900
area = [[1, 0], [-1, 0], [0, 0], [-1, -1], [0, -1]]

layer = {} # 2 for (0, 0) mask position
layer['Active'] = 2
layer['PNP-block'] = 2
layer['InGaAs'] = 2
layer['P-open'] = 2
layer['Metal'] = 2
layer['Wafer'] = 2