def is_harshad(number):
    sumed = sum(int(d) for d in str(number))
    return number % sumed == 0

def harshad_value(number):
    while number > 0:
        if is_harshad(number):
            return number
        number -= 1
    return 0

def harshad_dict(input_dict):
    return {key: harshad_value(key) for key in input_dict}

user_input = input().strip()
input_dict = eval(user_input)

result = harshad_dict(input_dict)

print(result)
