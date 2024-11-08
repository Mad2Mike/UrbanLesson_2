class Car:


    def __init__(self, model: str, __vin: int, __numbers: str):
        self.model = model
        self.__vin = __vin
        self.__is_valid_vin(__vin)
        self.__numbers = __numbers
        self.__is_valid_numbers(__numbers)

    def __is_valid_vin(self, __vin):
        if not isinstance(__vin, int):
            raise IncorrectVinNumber(message="Некорректный тип vin номер")
        elif __vin not in range(1000000, 10000000):
            raise IncorrectVinNumber(message="Неверный диапазон для vin номера")
        return True

    def __is_valid_numbers(self, __numbers):
        if not isinstance(__numbers, str):
            raise IncorrectCarNumbers(message="Некорректный тип данных для номеров")
        elif len(__numbers) != 6:
            raise IncorrectCarNumbers(message="Неверная длина номера")
        return True



class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message


try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')
