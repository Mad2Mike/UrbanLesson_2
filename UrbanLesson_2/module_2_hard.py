def pas_unlock(pas_number):
    # Функция для подбора пароля
    password = []
    list_numbers = list(range(1, pas_number))

    for i in list_numbers:
        for j in list_numbers:
            if i < j:
                if pas_number % (i + j) == 0:
                    password.append(i)
                    password.append(j)
    pas_to_str = ''.join(map(str, password))
    return pas_to_str


def number_check(pas_number):
    # Функция для проверки на ввод числа, соответствующего параметрам
    check_list = list(range(3, 21))

    try:
        number = int(pas_number)
        if number in check_list:
            return
        else:
            print("Вы ввели некорректное число")
            main()
    except ValueError:
        print("Это не число.")
    main()



def main():
    pas_number = input('Введите число от 3 до 20:')
    number_check(pas_number)
    print(f'Ваш пароль: {pas_unlock(int(pas_number))}')
    exit()


if __name__ == "__main__":
    main()
