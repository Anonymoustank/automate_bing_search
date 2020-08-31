import os
import time
import sys
error = 0
number = 100
loop_num = 20

if len(sys.argv) > 1:
    try:
        loop_num = int(sys.argv[1])
    except:
        print("Make sure the number passed is a positive integer")
        exit(1)

if loop_num <= 0:
    print("Make sure the number passed is a positive integer")
    exit(1)

for i in range(loop_num):
    if os.system('xdg-open "http://www.bing.com/search?q=f%s"' % number) != 0:
        error += 1
    number += 1
    if number % 5 == 0:
        time.sleep(5)
    else:
        time.sleep(1.5)

print("This program ran into %s errors" % error)
time.sleep(2)

