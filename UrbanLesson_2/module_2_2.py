first = int(input('Введите первое число:'))
second = int(input('Введите второе число:'))
third = int(input('Введите второе число:'))

list_base = [first, second, third]
list_equal = set(list_base)
list_equal_new = list(list_equal)


if len(list_equal_new) == 1:
    print('3')
elif len(list_equal_new) > 1 and len(list_equal_new) < len(list_base):
    print('2')
elif list_base == list_equal_new:
    print('0')

