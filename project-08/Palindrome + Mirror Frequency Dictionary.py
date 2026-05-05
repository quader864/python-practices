
def check_palindrome_mirror(input_dict):
    output = {}

    for key in input_dict:
        s = str(key)
        is_palindrome = s == s[::-1]
        freq = {}
        for digit in s:
            freq[digit] = freq.get(digit, 0) + 1
        freq_list = [freq[d] for d in sorted(freq)]
        is_mirror = freq_list == freq_list[::-1]


        output[key] = "YES" if is_palindrome and is_mirror else "NO"

    return output

text = input().strip()

text = text[1:-1]
items = [item.strip() for item in text.split(",") if ":" in item]

input_dict = {}
for item in items:
    key_str, _ = item.split(":")
    key = int(key_str.strip())
    input_dict[key] = None

result = check_palindrome_mirror(input_dict)
print(result)
