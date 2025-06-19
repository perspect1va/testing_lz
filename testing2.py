from testing_lz import gang

#Ручн тестирование
def gang_man_tests():
    print("Ручное тестирование:")
    test_cases = [
        (2, 3, 4),
        (1, 2, 3),
        (3, 2, 4),
        (0.5, 2, 1),
        (10, 5, 5),
        (5, 2, 1)
    ]
    for i, (a, b, c) in enumerate(test_cases, start=1):
        result = gang(a, b, c)
        print(f"Тест {i}: a={a}, b={b}, c={c} → {result}")
    print()
