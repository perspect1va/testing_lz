from testing_lz import gang

def gang_man_tests():
    print("Ручное тестирование:")
    test_cases = [
        (2, 3, 1),    
        (0, 2, 1),    
        (1, 2, 3),    
        (2, 2, 2),    
        (0.5, 2, 1),   
        (5, 2, 1)      
    ]
    
    for i, (a, b, c) in enumerate(test_cases, 1):
        result = gang(a, b, c)
        print(f"Тест {i}: a={a}, b={b}, c={c} → {result}")
    print()