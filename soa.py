import cfg
import dxf
import dev
import key

xsize = cfg.size
ysize = 100

def device(x, y, length):

  wg = 1
  l1 = 300
  l2 = 200
  l3 = 50

  idev = len(cfg.data)

  x1, y1 = dxf.srect('core', x, y, l1, cfg.wt)
  x2, y2 = dxf.taper('core', x1, y1, l2, cfg.wt, wg)
  x3, y3 = dxf.taper('core', x2, y2, l3, wg, cfg.wg)
  x4, y4 = dxf.sline('core', x3, y3, length)
  x5, y5 = dxf.taper('core', x4, y4, l3, cfg.wg, wg)
  x6, y6 = dxf.taper('core', x5, y5, l2, wg, cfg.wt)
  x7, y7 = dxf.srect('core', x6, y6, l1, cfg.wt)
  
  x7, y7 = dxf.srect('edge', x, y, x7 - x, 6)
  x7, y7 = dxf.srect('slab', x, y, x7 - x, 10)

  for i in range(4):
    dxf.srect('gold', x3 + i * 250 + 25, y3, 200, 85)
  
  dxf.move(idev, x, y, x7, y7, 0, 0, 7)

  dev.texts((x + x7) * 0.5, y, 'soa', 0.5, 'cc')
  
if __name__ == '__main__':

  device(3453.7, 3371.5, 1000)
  key.under(2152, 1875)

  dev.saveas('soa')