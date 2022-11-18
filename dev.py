import os
import dxf
import numpy as np

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

if __name__ == '__main__':

  dxf.texts(0, 0, 'test', 1, 'lb')

  saveas('text')