import os
import cfg
import dxf
import tip
import numpy as np

def texts(x, y, title, scale, align):

  if align[0] == 'l': x = x + 10
  if align[0] == 'r': x = x - 10

  l, w = dxf.texts('core', x, y, title, scale, align)

  if align[0] == 'l': xalign = x - 10
  if align[0] == 'c': xalign = x - l * 0.5 - 10
  if align[0] == 'r': xalign = x - l - 10

  # dxf.srect('edge', xalign, y, l + 20, w + 20)

def arange(start, stop, step):

  return np.arange(start, stop + step * 0.5, step)

def move(idev, x, xp, length):

  ltip = (length - xp + x) * 0.5

  if ltip < tip.ltip: ltip = tip.ltip

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

if __name__ == '__main__':

  texts(0, 0, 'test', 1, 'lb')

  saveas('text')