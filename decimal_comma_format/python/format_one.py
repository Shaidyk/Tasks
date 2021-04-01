def format_digits_concatenation(value):
    if value < 0:
        raise ValueError

    value_len = len(str(value))
    coma_place = 0
    for i in range(value_len):
        if i == value_len - 1:
            break
        if (-(i + 1) % 3) == 0:
            i += coma_place
            value = str(value)[:-(i + 1)] + ',' + str(value)[-(i + 1):]
            coma_place += 1
    return value


value_list = [1000, 200, 1234567]
for value in value_list:
    print(format_digits_concatenation(value))
