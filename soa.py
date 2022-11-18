import cfg
import dxf
import dev
import key
import numpy as np

xsize = 2000
ysize = 600

def device(x, y, length, width):

  wg, ltip, ltaper, lexpand = 1, 10, 200, 50

  angle = np.cos(cfg.tilt * np.pi / 180)
  xtilt = (length + 40) / angle
  ytilt = xtilt * np.tan(cfg.tilt * np.pi / 180)
  lchip = xtilt - (ltip + ltaper + lexpand) * 2

  idev = len(cfg.data)

  x1, y1 = x - 20 / angle, y - (ytilt - ysize) * 0.5
  x2, y2 = dxf.srect('Active', x1, y1, ltip, cfg.wt)
  x3, y3 = dxf.taper('Active', x2, y2, ltaper, cfg.wt, wg)
  x4, y4 = dxf.taper('Active', x3, y3, lexpand, wg, width)
  x5, y5 = dxf.srect('Active', x4, y4, lchip, width)
  x6, y6 = dxf.taper('Active', x5, y5, lexpand, width, wg)
  x7, y7 = dxf.taper('Active', x6, y6, ltaper, wg, cfg.wt)
  x8, y8 = dxf.srect('Active', x7, y7, ltip, cfg.wt)
  
  dxf.srect('P-open', x1 + 5, y1, x8 - x1 - 10, 6)
  dxf.srect('InGaAs', x1, y1, x8 - x1, 10)
  dxf.srect('Metal', x4, y4, lchip, 100)

  l, w = 180, 90

  for yt in [115, -115]:
    for xt in [0, l + 20]:
      dxf.srect('Metal', x4 + xt, y4 + yt, l, w)
      dxf.srect('Metal', x5 - xt - l, y4 + yt, l, w)

  dxf.move(idev, x1, y1, x8, y8, 0, 0, cfg.tilt)

  edge(x, y)

  return x + xsize, y + ysize

def edge(x, y):

  w, g = 10, 5

  x1, y1 = x + g, y + g
  x2, y2 = x - g + xsize, y - g + ysize

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

def chip(x, y, length, width):

  for i in range(13):
    x1, y1 = x, y + i * ysize
    x2, y2 = device(x1, y1, length, width)

    s = 'soa-' + str(length) + '-' + str(width) + '-' + str(i+1)
    dxf.texts('Metal', x1 + length * 0.5, y1 + 20, s, 0.5, 'cb')

  return x2, y2

if __name__ == '__main__':

  chip(3500, 3000, xsize, cfg.wg)

  key.chips(3650, 1850)
  key.chips(3650, 1850 + 9800)

  dev.saveas('soa')