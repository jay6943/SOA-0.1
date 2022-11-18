import os
import dxf
import numpy as np

def edge(layer, x, y, length, width):

  w, g = 10, 5

  x1, y1 = x + g, y + g
  x2, y2 = x - g + length, y - g + width

  dxf.rects(layer, x1, y1, x1 + w, y1 + w)
  dxf.rects(layer, x1, y2, x1 + w, y2 - w)
  dxf.rects(layer, x2, y1, x2 - w, y1 + w)
  dxf.rects(layer, x2, y2, x2 - w, y2 - w)

  dx, dy, w = 50, 50, 40

  dxf.crect(layer, x1 + dx, y1 + dy, w, w)
  dxf.crect(layer, x2 - dx, y2 - dy, w, w)

  dx, l = 50, 70
  dy, w = 50, 14

  dxf.crect(layer, x1 + dx, y2 - dy, l, w)
  dxf.crect(layer, x1 + dx, y2 - dy, w, l)
  dxf.crect(layer, x2 - dx, y1 + dy, l, w)
  dxf.crect(layer, x2 - dx, y1 + dy, w, l)

def arange(start, stop, step):

  return np.arange(start, stop + step * 0.5, step)

def move(idev, x, xp, length):

  ltip = (length - xp + x) * 0.5

  xtip, _ = dxf.move(idev, x, 0, xp, 0, ltip, 0, 0)

  return xtip, ltip

def removes(folder):

  if os.path.isdir(folder):
    
    files = os.listdir(folder)
    
    for fp in files:
      if os.path.exists(folder + fp): os.remove(folder + fp)
    
    os.rmdir(folder)

def saveas(filename):

  fp = dxf.start(filename)
  dxf.conversion(fp)
  dxf.close(fp)

  removes('__pycache__/')