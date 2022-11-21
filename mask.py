import cfg
import dxf
import dev
import soa
import amp
import lds
import key

if __name__ == '__main__':

  x1, y1 = 3500, 3000
  x2, y2 = x1, 12745

  for _ in range(3): x1, _ = soa.chip(x1, y1, 1000, cfg.wg)
  x3, _ = amp.chip(x2, y2, 1000, cfg.wg)
  x4, _ = lds.chip(x3, y2, 400, cfg.wg)

  key.chips(3650, 1850)
  key.chips(3650, 1850 + 9800)

  dxf.circle('Wafer', 0, 0, 25400, 0, 90, 91)
  dxf.circle('Wafer', 25400, 0, 25400, 90, 180, 91)

  dev.saveas('mask')