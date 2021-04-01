def format_digits(value):
    return "{:,d}".format(value)


value_list = [1000, 200, 1234567]
for value in value_list:
    print(format_digits(value))
