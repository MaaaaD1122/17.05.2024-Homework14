def test(*args, **kwargs):
    for i in args:
        print(i)
    for key, value in kwargs.items():
        print(f"{key}: {value}")
test("Здравствуйте", name="Максим", age=27)

def test_2(n):
    if n == 0:
        return 0
    else:
        return n + test_2(n - 1)
n = 5
result = test_2(n)
print(f"Результат от {n} является {result}")