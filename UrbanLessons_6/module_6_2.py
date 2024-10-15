class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner: str, __model: str, __engine_power: int, __color: str):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        return f"Модель: {self.__model}"
    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"
    def get_color(self):
        return f"Цвет: {self.__color}"
    def set_color(self, new_color: str):
        color_variants_lower = [color.lower() for color in self.__COLOR_VARIANTS]
        if new_color.lower() in color_variants_lower:
            self.__color = new_color
        else:
            print("Нельзя сменить цвет на <новый цвет>")
            return




    def print_info(self):
        return print(f"{Vehicle.get_model(self)}"
                     f"\n{Vehicle.get_horsepower(self)}"
                     f"\n{Vehicle.get_color(self)} "
                     f"\nВладелец: {self.owner}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()