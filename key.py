import cfg
import dxf
import dev

def upper(layer, x, y):

  l, w, g, h = 22, 8, 11, 50

  for i in range(4):

    y1 = y + i * g + w * 0.5 - 84

    dxf.srect(layer, x - 11, y1, l, w)
    dxf.srect(layer, x - 11, y1 + 55, l, w)

    x2 = x - 49 + i * g
    y2 = y + 49 + l * 0.5

    dxf.srect(layer, x2, y2, w, l)
    dxf.srect(layer, x2 + 55, y2, w, l)

  dxf.srect(layer, x - 25, y - 40 + w * 0.5, h, w)
  dxf.srect(layer, x - 5, y + 35 + h * 0.5, w, h)

def under(layer, x, y):

  l, w, g = 20, 8, 12

  for i in range(9):

    y1 = y + i * g + w * 0.5 - 88

    dxf.srect(layer, x - 35, y1, l, w)
    dxf.srect(layer, x + 15, y1, l, w)

    x2 = x - 53 + i * g
    y2 = y + 25 + l * 0.5

    dxf.srect(layer, x2, y2, w, l)
    dxf.srect(layer, x2, y2 + 50, w, l)

def cross(layer, x, y):

  l = 300
  w = 50

  dxf.crect(layer, x, y, l, w)
  dxf.crect(layer, x, y, w, l)
  dxf.crect(layer, x, y + 250, 100, 1)

def device(layer, x, y, n, label):

  cross(layer, x, y)

  if layer == 'Metal': dxf.texts(layer, x + 200, y, label, 2, 'lc')

  upper(layer, x - 1785 + (n - 1) * 170, y)
  under(layer, x - 1785 + (n - 0) * 170, y)

def chip(layer, x, y, n, label):

  for i in range(7):
    xi = x + i * 3000
    device(layer, xi, y, n, str(i + 1))
    dxf.srect('PNP-block', xi - 1980, y, 450, 300)

  xt, yt = 28000, 12000

  idev = len(cfg.data)
  x1, y1 = dxf.texts(layer, xt, yt, label, 15, 'cb')
  dxf.move(idev, xt, yt, xt + x1, yt + y1, 0, 0, 270)

def chips(x, y):

  i = 0
  
  for layer in cfg.layer:
    
    i = i + 1
    
    chip(layer, x, y, i, layer)
    
  dxf.crect('Active', x, y + 200, 40, 2)

if __name__ == '__main__':

  chips(3650, 1850)

  dev.saveas('soa')