def format_digits(value):
    source = "{:,d}"
    return source.format(value)


value_list = [1000, 200, 1234567]
for value in value_list:
    print(format_digits(value))


import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
print('{:n}'.format(1234567))
