import math
import time
a = 1000000
denom = math.log(10)
t0 = time.time()
for i in range(1,a):
    py_len = len(str(i))
t1 = time.time()
for i in range(1,a):
    math_len = math.floor(math.log(i)/denom)+1
t2 = time.time()
for i in range(1,a):
    math_len = math.floor(math.log10(i))+1
t3 = time.time()
for i in range(1,a):
    math_len = math.ceil(math.log10(i))
t4 = time.time()
for i in range(1,a):
    math_len = int(math.log10(i))+1
t5 = time.time()
print(f"pytime:{t1-t0}\n mathtime:{t2-t1}\n math10time: {t3-t2}\n math10ceiltime:{t4-t3}\n math10intcast:{t5-t4}")


a = 1000000
b = 123456
denom = math.log(10)
t0 = time.time()
for i in range(1,a):
    digits = math.ceil(math.log10(i))
    result = b*(10**digits) + a
t1 = time.time()
for i in range(1,a):
    result = b*(10**math.ceil(math.log10(i))) + a
t2 = time.time()
for i in range(1,a):
    int(str(a) + str(b))
t3 = time.time()
print(f"math:{t1-t0}\n mathoneline:{t2-t1}\n pytime: {t3-t2}\n")
