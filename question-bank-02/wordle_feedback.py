def wordle_feedback(key: str, guess: str) -> str:
    """تولید رنگ‌بندی برای هر حدس (بدون در نظر گرفتن حالت پایان بازی)"""
    result = ['R'] * len(key)
    key_remaining = list(key)

    # مرحله 1: سبزها (G)
    for i, ch in enumerate(guess):
        if ch == key[i]:
            result[i] = 'G'
            key_remaining[i] = None  # حذف از کلید برای مرحله بعد

    # مرحله 2: زردها (Y)
    for i, ch in enumerate(guess):
        if result[i] == 'R' and ch in key_remaining:
            result[i] = 'Y'
            key_remaining[key_remaining.index(ch)] = None

    return ''.join(result)


# -------------------------------
# 📥 خواندن ورودی طبق فرمت پروژه
# -------------------------------
key = input().strip()
q = int(input().strip())

game_over = False  # وضعیت پایان بازی

for _ in range(q):
    guess = input().strip()

    # اگر بازی قبلاً تمام شده باشد
    if game_over:
        print("Game Over")
        continue

    # بررسی طول نادرست
    if len(guess) != len(key):
        print("Invalid Length")
        continue

    # بررسی حدس درست
    if guess == key:
        print('G' * len(key))
        game_over = True
        continue

    # حدس معمولی
    print(wordle_feedback(key, guess))
