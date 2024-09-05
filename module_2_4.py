import time

# Мое решение

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
start_time = time.perf_counter()


for i in numbers:
    count_b = 0
    for j in range(1, (i+1)):
        b = (i % j)
        if b == 0:
            count_b += 1

    if count_b == 2:
        primes.append(i)
    elif count_b != 2 and i != 1:
        not_primes.append(i)


end_time = time.perf_counter()
execution_time = end_time - start_time
print(primes)
print(not_primes)

print(f"Время выполнения функции: {execution_time} секунд")





# Решение нейросети

numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Создание пустых списков для простых и непростых чисел
primes2 = []
not_primes2 = []

start_time = time.perf_counter()
# Перебор списка numbers
for num in numbers2:
    # Предполагаем, что число простое
    is_prime = True

    # Числа меньше 2 не являются простыми
    if num < 2:
        is_prime = False
    else:
        for divisor in range(2, num):  # Проверяем делители от 2 до num-1
            if num % divisor == 0:
                is_prime = False
                break

    # Добавление числа в соответствующий список
    if is_prime:
        primes2.append(num)
    else:
        not_primes2.append(num)

# Вывод списков
print("Простые числа:", primes2)
print("Непростые числа:", not_primes2)
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Время выполнения функции: {execution_time} секунд")
