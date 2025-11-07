# خواندن مقادیر اولیه
n, q, l = map(int, input().split())

# ساخت دیکشنری برای ذخیره داده‌ها
data = {}

# خواندن n رشته باینری و مقدار Y/N مربوط به آن‌ها
for _ in range(n):
    binary_str, label = input().split()
    data[binary_str] = label

# بررسی q رشته ورودی و چاپ نتیجه
for _ in range(q):
    query = input().strip()
    if query in data:
        print(data[query])
    else:
        print("Unknown")
