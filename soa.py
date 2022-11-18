import cfg
import dxf
import dev
import key
import numpy as np

xsize = 1000
ysize = 600
angle = np.cos(cfg.tilt * np.pi / 180)
slope = np.tan(cfg.tilt * np.pi / 180)

def srect(layer, x, y, length, width):

  w = width * 0.5
  dx = width * slope * 0.5

  data = [layer]

  data.append([x - dx, y - w])
  data.append([x - dx + length, y - w])
  data.append([x + dx + length, y + w])
  data.append([x + dx, y + w])

  cfg.data.append(data)

  return x + length, y

def device(x, y, length, width):

  wg, ltip, ltaper, lexpand = 1, 40, 200, 50

  ytilt = (length + ltip) / angle * slope
  lchip = (length + ltip) / angle - (ltip + ltaper + lexpand) * 2

  idev = len(cfg.data)

  x1, y1 = x - ltip * 0.5 / angle, y - (ytilt - ysize) * 0.5
  x2, y2 = dxf.srect('Active', x1, y1, ltip, cfg.wt)
  x3, y3 = dxf.taper('Active', x2, y2, ltaper, cfg.wt, wg)
  x4, y4 = dxf.taper('Active', x3, y3, lexpand, wg, width)
  x5, y5 = dxf.srect('Active', x4, y4, lchip, width)
  x6, y6 = dxf.taper('Active', x5, y5, lexpand, width, wg)
  x7, y7 = dxf.taper('Active', x6, y6, ltaper, wg, cfg.wt)
  x8, y8 = dxf.srect('Active', x7, y7, ltip, cfg.wt)
  
  dxf.srect('P-open', x1 + 5, y1, x8 - x1 - 10, 6)
  dxf.srect('InGaAs', x1, y1, x8 - x1, 10)
  
  srect('Metal', x + 5, y1, x8 - x - ltip * 0.5 - 10, 100)

  l, w = 180, 90
  xc = x1 + (x8 - x1) * 0.5
  dx = (x8 - x1) * 0.15
  dy = 115

  for yt in [1, -1]:
    for xt in [1, -1]:
      dxf.crect('Metal', xc + xt * dx, y4 + yt * dy, l, w)
      dxf.crect('Metal', xc + xt * (dx + 200), y4 + yt * dy, l, w)
    dxf.crect('Metal', xc + yt * dx, y4 + yt * 60, 50, 20)

  dxf.move(idev, x1, y1, x8, y8, 0, 0, cfg.tilt)

  dev.edge('Metal', x, y, xsize, ysize)

  return x + xsize, y + ysize

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