class Car:
    def __init__(self, model: str, vin: int, numbers: str):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers
        self.__is_valid_vin(self.__vin)
        self.__is_valid_numbers(self.__numbers)

    def __is_valid_vin(self, vin: int):
        if isinstance(vin, int) == False:
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if vin < 1000000 or vin > 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            return True

    def __is_valid_numbers(self, numbers: str):
        if isinstance(numbers, str) != True:
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        else:
            return True

class IncorrectVinNumber(Exception):
    def __init__(self, massage):
        self.massage = massage

class IncorrectCarNumbers(Exception):
    def __init__(self, massage):
        self.massage = massage

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.massage)
except IncorrectCarNumbers as exc:
  print(exc.massage)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.massage)
except IncorrectCarNumbers as exc:
  print(exc.massage)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.massage)
except IncorrectCarNumbers as exc:
  print(exc.massage)
else:
  print(f'{third.model} успешно создан')