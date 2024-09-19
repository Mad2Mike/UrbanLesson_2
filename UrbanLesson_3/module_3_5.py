
def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])



    if len(str_number) > 1:
        if first == 0:  # Игнорируем ноль
            return get_multiplied_digits(int(str_number[1:]))

        elif:
            return first * get_multiplied_digits(int(str_number[1:]))

        else:
            return first


result = get_multiplied_digits(2030)
print(result)

