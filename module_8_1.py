def add_everything_up(a, b):
    """
    Складывает числа и строки, обрабатывая несовместимые типы.
    """
    try:
        return round(a + b, 3)  # Округление до 3 знаков после запятой
    except TypeError:
        return str(a) + str(b)
    except OverflowError:
        return "Результат операции выходит за пределы допустимого диапазона"


# Пример использования
print(add_everything_up(123.456, 'строка'))  # Вывод: 123.456строка
print(add_everything_up('яблоко', 4215))  # Вывод: яблоко4215
print(add_everything_up(123.456, 7))  # Вывод: 130.456

