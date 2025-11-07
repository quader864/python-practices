def game(number):
    # جدا کردن دو رقم عدد
    tens = number // 10   # رقم دهگان
    ones = number % 10    # رقم یکان

    # محاسبه تفاضل مطلق بین دو رقم
    return abs(tens - ones)
