def print_params(a=1, b='строка', c=True):
    print(a, b, c)
    pass


values_list = [42, False, "Это тоже строка"]
values_dict = {'a': 491, 'b': 1.2313, 'c': 'This is not true', }
values_list_2 = [54.32, 'Строка']

print('1:\n')
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

print('\n2:\n')
print_params(*values_list)
print_params(**values_dict)

print('\n3:\n')
print_params(*values_list_2, 42)
