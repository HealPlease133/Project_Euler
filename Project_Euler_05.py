# 1 ~ 10 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 2520입니다.

# 그러면 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 얼마입니까?

def isPrime(num):
    primes = []
    while num != 1:
        for i in range(2,num + 1):
            if num % i == 0:
                primes.append(i)
                num //= i
    return primes
        
def solution(num):
    maxcnt2 = 0
    maxcnt3 = 0
    maxcnt5 = 0
    result = 1
    temps = []
    for i in range(2, num +1):
        cnt2 = 0
        cnt3 = 0
        cnt5 = 0
        temp = isPrime(i)
        for k in temp:
            if k == 2:
                cnt2 += 1
            elif k == 5:
                cnt5 += 1
            elif k == 3:
                cnt3 += 1
            else:
                if k in temps:
                    continue
                result *= k
                temps.append(k)
        if maxcnt2 < cnt2:
            maxcnt2 = cnt2
        if maxcnt3 < cnt3:
            maxcnt3 = cnt3
        if maxcnt5 < cnt5:
            maxcnt5 = cnt5
    result *= (5 ** maxcnt5) * (2 ** maxcnt2) * (3 ** maxcnt3)
    return result
    
print(solution(20))
