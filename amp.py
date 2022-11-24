import cfg
import dxf
import dev

ysize = 500

def chip(x, y, length):

  wg, ltip, ltaper, lexpand = 1, 40, 200, 50

  lchip = length - ltip - (ltaper + lexpand) * 2

  x1, y1 = x - ltip * 0.5, y + ysize * 0.5
  x2, y2 = dxf.srect('active', x1, y1, ltip, cfg.wt)
  x3, y3 = dxf.taper('active', x2, y2, ltaper, cfg.wt, wg)
  x4, y4 = dxf.taper('active', x3, y3, lexpand, wg, cfg.wg)
  x5, y5 = dxf.srect('active', x4, y4, lchip, cfg.wg)
  x6, y6 = dxf.taper('active', x5, y5, lexpand, cfg.wg, wg)
  x7, y7 = dxf.taper('active', x6, y6, ltaper, wg, cfg.wt)
  x8, y8 = dxf.srect('active', x7, y7, ltip, cfg.wt)
  
  dxf.srect('p-open', x1 + 5, y1, x8 - x1 - 10, 6)
  dxf.srect('ingaas', x1, y1, x8 - x1, 10)
  dev.metal('metal', x, y1, length, 300)
  dev.metal('plate', x, y1, length, 300)

  dev.edge('metal', x, y, length, ysize)

  return x + length, y + ysize

def chips(x, y):

  for i in range(4):
    length = 500 + 500 * i

    for j in range(15):
      x1, y1 = x, y + j * ysize
      x2, y2 = chip(x1, y1, length)

      s = 'amp-' + str(length) + '-' + str(j+1)
      dxf.texts('metal', x1 + length * 0.5, y1 + 30, s, 0.5, 'cb')

    x = x2

  return x2, y2

if __name__ == '__main__':

  chips(0, 0)

  dev.saveas('amp')