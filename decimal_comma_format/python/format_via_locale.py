import locale

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

value_list = [1000, 200, 1234567]
for value in value_list:
    print('{:n}'.format(value))
