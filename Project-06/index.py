import math

n = int(input().strip())
original = n

sum_factorials = 0

while n > 0:
    digit = n % 10
    sum_factorials += math.factorial(digit)
    n //= 10

if sum_factorials == original:
    print("YES")
else:
    print("NO")
