def calculator(n, m, li):
    return sum(sum(li[i:i+m]) * (1 if (i//m)%2==0 else -1) for i in range(0, n, m))