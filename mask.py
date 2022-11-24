import dxf
import dev
import soa
import amp
import lds
import key

if __name__ == '__main__':

  x1, y1 = 3700, 3000
  x2, y2 = x1, 12745

  x2, _ = lds.chips(x1, y1)
  for _ in range(3): x2, _ = soa.chips(x2, y1)
  x2, _ = lds.chips(x2, y1)

  x2, _ = lds.chips(x1, y2)
  x2, _ = soa.chips(x2, y2)
  x2, _ = amp.chips(x2, y2)
  x2, _ = soa.chips(x2, y2)
  x2, _ = lds.chips(x2, y2)

  key.chips(4450, 1850)
  key.chips(4450, 1850 + 9800)

  dxf.circle('wafer', 0, 0, 25400, 0, 90, 91)
  dxf.circle('wafer', 25400, 0, 25400, 90, 180, 91)

  dev.saveas('SOA V0.1')