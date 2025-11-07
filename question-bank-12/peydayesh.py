def find(num1, num2, num3):
    all_numbers = {1, 2, 3, 4}
    chosen = {num1, num2, num3}
    missing = all_numbers - chosen
    return missing.pop()
