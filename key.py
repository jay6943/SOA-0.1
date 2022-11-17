import cfg
import dxf
import dev

def under(x, y):

  l = 20
  w = 8
  g = 12

  for i in range(9): dxf.srect('core', x + i * g, y, w, l)