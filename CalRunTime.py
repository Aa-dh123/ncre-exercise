#CalRunTime.py

import time

limit = 10*1000*1000
start = time.perf_counter()
while True:
    limit -= 1
    if limit <= 0:
        break

end = time.perf_counter()
delta = end - start
print(start)
print(end)
print("程序运行时间是：{}秒".format(delta))
