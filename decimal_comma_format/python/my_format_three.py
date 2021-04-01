def format_digits_list_insert(value):
    if value < 0:
        raise ValueError

    v_list = list(str(value))
    value_len = len(str(value))
    coma_place = 0
    for i in range(value_len):
        if -(i + 1) % 3 == 0:
            if value_len - i == 1:
                break
            i += coma_place
            v_list.insert(-(i + 1), ',')
            coma_place += 1
    result = ''.join(v_list)
    return result


value_list = [1000, 200, 1234567]
for value in value_list:
    print(format_digits_list_insert(value))
