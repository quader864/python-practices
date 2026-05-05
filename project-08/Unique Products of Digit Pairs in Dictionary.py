text = ""
while True:
    text += input().strip()
    if "}" in text:
        break

text = text.strip()[1:-1]
items = [item.strip() for item in text.split(",") if ":" in item]

result = {}

for item in items:
    key_str, _ = item.split(":")
    key = int(key_str.strip())
    digits = str(key)
    products = []

    ok = True

    for i in range(0, len(digits) - 1, 2):
        a = int(digits[i])
        b = int(digits[i+1])
        p = a * b
        if p in products:
            ok = False
            break
        products.append(p)

    result[key] = "YES" if ok else "NO"

print(result)
