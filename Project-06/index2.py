def is_harshad(num):
    digit_sum = sum(int(d) for d in str(num))
    return num % digit_sum == 0

n = int(input().strip())

if is_harshad(n):
    print(n)
else:
    # Find the largest Harshad number smaller than n
    for x in range(n - 1, 0, -1):
        if is_harshad(x):
            print(x)
            break
