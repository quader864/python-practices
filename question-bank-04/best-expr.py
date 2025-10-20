expr = input().strip()

# جدا کردن اعداد از عبارت
a, b, c = map(int, expr.split('?'))

ops = ['+', '*']
best = 0

for op1 in ops:
    for op2 in ops:
        # دو حالت پرانتزگذاری
        expr1 = eval(f"({a}{op1}{b}){op2}{c}")
        expr2 = eval(f"{a}{op1}({b}{op2}{c})")
        best = max(best, expr1, expr2)

print(best)
