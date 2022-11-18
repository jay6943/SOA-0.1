import cfg
import dev
import soa
import amp
import lds
import key

if __name__ == '__main__':

  x1, y1 = 3500, 3000

  for _ in range(3): x1, _ = soa.chip(x1, y1, 1000, cfg.wg)
  x2, _ = amp.chip(x1 + 100, y1, 1000, cfg.wg)
  x3, _ = lds.chip(x2 + 100, y1, 400, cfg.wg)

  key.chips(3650, 1850)
  key.chips(3650, 1850 + 9800)

  dev.saveas('mask')