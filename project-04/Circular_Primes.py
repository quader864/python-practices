import sys

def sieve_bool(limit):
    # is_prime[i] = True iff i is prime, for 0 <= i <= limit
    is_prime = [True] * (limit + 1)
    if limit >= 0:
        is_prime[0] = False
    if limit >= 1:
        is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            step = i * i
            is_prime[step: limit + 1: i] = [False] * (((limit - step) // i) + 1)
    return is_prime

def rotations_of_number(x):
    s = str(x)
    n = len(s)
    for i in range(n):
        yield int(s[i:] + s[:i])

def count_circular_primes(n):
    if n <= 2:
        return 0
    # برای پوشش همه‌ی چرخش‌ها، تا 10^d غربال می‌سازیم
    max_digits = len(str(max(1, n-1)))
    limit = 10 ** max_digits  # پوشش کافی برای تمام چرخش‌ها
    is_prime = sieve_bool(limit)

    count = 0
    for p in range(2, n):
        if not is_prime[p]:
            continue
        ok = True
        for r in rotations_of_number(p):
            if r > limit or not is_prime[r]:
                ok = False
                break
        if ok:
            count += 1
    return count

if __name__ == "__main__":
    data = sys.stdin.read().strip().split()
    if not data:
        sys.exit(0)
    n = int(data[0])
    print(count_circular_primes(n))
