num_str = ""
while True:
    try:
        line = input().strip()
        if not line:
            break
        num_str += line
    except EOFError:
        break
max_product = 0
max_sequence = ""
n = 13
for i in range(len(num_str) - n + 1):
    seq = num_str[i:i + n]
    if '0' in seq:
        product = 0
    else:
        product = 1
        for ch in seq:
            product *= int(ch)
    if product > max_product:
        max_product = product
        max_sequence = seq
print(max_sequence)
