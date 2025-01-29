# 10보다 작은 자연수 중에서 3 또는 5의 배수는 3, 5, 6, 9 이고, 이것을 모두 더하면 23입니다.

# 1000보다 작은 자연수 중에서 3 또는 5의 배수를 모두 더하면 얼마일까요?

def getNum(num):
    nums = []
    for i in range(1,num):
        if i % 3 == 0 and i not in nums:
            nums.append(i)
        elif i % 5 == 0 and i not in nums:
            nums.append(i)
    return sum(nums)

print(getNum(1000))
