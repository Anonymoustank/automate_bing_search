import os
import time
number = 100

for i in range(5):
    for i in range(4):
        os.system('/data/data/com.termux/files/usr/bin/xdg-open "http://www.bing.com/search?q=%s"' % number)
        number += 1
        time.sleep(1.5)
    time.sleep(5)
