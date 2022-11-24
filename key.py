import cfg
import dxf
import dev

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

def cross(layer, x, y):

  l = 300
  w = 50

  dxf.crect(layer, x, y, l, w)
  dxf.crect(layer, x, y, w, l)
  dxf.crect(layer, x, y + 250, 100, 1)

def label(layer):

  x, y = 28000, 12000

  title = 'lo-v1.0-' + layer

  idev = len(cfg.data)
  x1, y1 = dxf.texts(layer, x, y, title, 15, 'cb')
  dxf.move(idev, x, y, x + x1, y + y1, 0, 0, 270)

def device(layer, x, y, dx):

  n = cfg.layer[layer]

  cross(layer, x, y)

  if cfg.layer[layer] > 0:
    upper(layer, x - dx + 170 * n, y)
    under(layer, x - dx + 170 * (n + 1), y)

def chip(x, y):

  dx = 1800

  for layer in cfg.layer:
    device(layer, x, y, dx)
    if layer != 'wafer': label(layer)
  
  xt = x - dx + 170 * (len(cfg.layer) + 1)

  under('active', xt, y)
  upper('pnp-block', xt, y)
  dxf.srect('pnp-block', x - dx, y, 1200, 300)

def chips(x, y):

  for i in range(7):
    xt = x + i * 3000
    chip(xt, y)
    dxf.texts('metal', xt + 200, y, str(i+1), 2, 'lc')

if __name__ == '__main__':

  chips(3650, 1850)

  dev.saveas('soa')