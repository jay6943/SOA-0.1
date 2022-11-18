import cfg
import dxf
import dev
import key

xsize = 1990
ysize = 490

def edge(x, y):

  x1, y1 = x, y
  x2, y2 = x + xsize, y + ysize

  w = 10

  dxf.rects('Metal', x1, y1, x1 + w, y1 + w)
  dxf.rects('Metal', x1, y2, x1 + w, y2 - w)
  dxf.rects('Metal', x2, y1, x2 - w, y1 + w)
  dxf.rects('Metal', x2, y2, x2 - w, y2 - w)

  dx, l = 110, 150
  dy, w = 35, 75

  dxf.rects('Metal', x1 + dx, y1 + dy, x1 + l, y1 + w)
  dxf.rects('Metal', x2 - dx, y2 - dy, x2 - l, y2 - w)

  dx, l = 145, 70
  dy, w = 70, 14

  dxf.crect('Metal', x1 + dx, y2 - dy, l, w)
  dxf.crect('Metal', x1 + dx, y2 - dy, w, l)
  dxf.crect('Metal', x2 - dx, y1 + dy, l, w)
  dxf.crect('Metal', x2 - dx, y1 + dy, w, l)

def device(x, y, length):

  wg = 1
  l1 = 300
  l2 = 200
  l3 = 50

  idev = len(cfg.data)

  x1, y1 = dxf.srect('Active', x, y, l1, cfg.wt)
  x2, y2 = dxf.taper('Active', x1, y1, l2, cfg.wt, wg)
  x3, y3 = dxf.taper('Active', x2, y2, l3, wg, cfg.wg)
  x4, y4 = dxf.sline('Active', x3, y3, length)
  x5, y5 = dxf.taper('Active', x4, y4, l3, cfg.wg, wg)
  x6, y6 = dxf.taper('Active', x5, y5, l2, wg, cfg.wt)
  x7, y7 = dxf.srect('Active', x6, y6, l1, cfg.wt)
  
  dxf.srect('P-open', x + 5, y, x7 - x - 10, 6)
  dxf.srect('InGaAs', x, y, x7 - x, 10)

  l = 180
  w = 90

  dxf.srect('Metal', x3, y3, length, 100)

  for yt in [115, -115]:
    for xt in [0, l + 20]:
      dxf.srect('Metal', x3 + xt, y3 + yt, l, w)
      dxf.srect('Metal', x4 - xt - l, y3 + yt, l, w)

  dxf.move(idev, x, y, x7, y7, 0, 0, 7)

  dxf.texts('Metal', (x + x7) * 0.5, y, 'soa', 0.5, 'cc')
  
if __name__ == '__main__':

  device(3453.7, 3371.5, 1000)

  edge(3505, 3255)

  key.chips(3650, 1850)

  dev.saveas('org')