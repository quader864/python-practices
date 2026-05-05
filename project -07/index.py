n = int(input().strip())

# اگر n < 1
if n < 1:
    print("NO")
    exit()

# اگر تک‌رقمی باشد
if n < 10:
    print("YES")
    exit()

# تبدیل عدد به رشته برای کار با ارقام
digits = [int(d) for d in str(n)]

# بیشترین رقم
max_digit = max(digits)

# محاسبه Digital Root
digital_root = n
while digital_root >= 10:
    digital_root = sum(int(d) for d in str(digital_root))

# مقایسه
if digital_root == max_digit:
    print("YES")
else:
    print("NO")
