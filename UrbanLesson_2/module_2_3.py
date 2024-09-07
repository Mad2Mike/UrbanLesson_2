my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0

while a < len(my_list):
    b = my_list[a]
    if b > 0:
        a += 1
        print(f'{b}')
    elif b == 0:
        a += 1
    else:
        print('Exit')
        break




