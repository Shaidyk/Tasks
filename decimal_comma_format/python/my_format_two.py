def format_digits_list_append(value):
    if value < 0:
        raise ValueError

    v_str = ''
    v_list = []
    for i in range(len(str(value))):
        v_str = v_str + str(value)[-(i + 1)]
        if len(v_str) == 3:
            v_list.append(v_str)
            v_str = ''
        elif len(str(value)) - i == 1:
            v_list.append(v_str)
    v_str = ','.join(v_list)
    result = ''.join(reversed(v_str))
    return result


value_list = [1000, 200, 1234567]
for value in value_list:
    print(format_digits_list_append(value))
