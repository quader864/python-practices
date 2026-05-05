def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
def check_strong_key(d):
    for key in d:
        value = d[key]
        if not is_prime(len(key)):
            return False

        if value <= 0 or value % 2 != 0:
            return False
    return True
user_input = input()
data = eval(user_input)
if check_strong_key(data):
    print("YES")
else:
    print("NO")
