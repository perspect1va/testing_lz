import math

def gang(a, b, c):
    try:
        if c**b == b**a:
            raise ZeroDivisionError("Знаменатель левого члена равен 0")
        if b - c <= 0:
            raise ValueError("Выражение под корнем должно быть положительным")
        if a <= 0:
            raise ValueError("Аргумент логарифма должен быть больше 0")

        term1 = a / (c**b - b**a)
        term2 = math.log(a) / math.sqrt(b - c)
        return term1 + term2

    except (ZeroDivisionError, ValueError) as e:
        return f"Ошибка при вычислении: {e}"
