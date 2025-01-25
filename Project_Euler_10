# 이백만 이하 소수의 합
# 10 이하의 소수를 모두 더하면 2 + 3 + 5 + 7 = 17 이 됩니다.
# 이백만(2,000,000) 이하 소수의 합은 얼마입니까?

import math

result = 0
num = 2000000
primes = []

for i in range(0, num + 1):
    primes.append(i)
primes[1] = 0

for i in range(0, num + 1):
    if primes[i] == 0:
        continue
    for k in range(i * 2, num + 1, i):
        primes[k] = 0

result = sum(primes)
print(result)
