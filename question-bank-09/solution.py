def fruits(tuple_of_fruits):
    good_fruits = {}
    for fruit in tuple_of_fruits:
        if (fruit['shape'] == 'sphere' and
            300 <= fruit['mass'] <= 600 and
            100 <= fruit['volume'] <= 500):
            name = fruit['name']
            good_fruits[name] = good_fruits.get(name, 0) + 1
    return good_fruits
