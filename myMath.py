# def add(a, b):
#     return a + b

# def sub(a, b):
#     return a - b

# def mul(a, b):
#     return a * b

# def div(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return "Нөлге бөлуге болмайды!"


import numpy as np

arr = np.random.randint(1, 100, 10)
print("Массив:", arr)
print("Орта мәні:", np.mean(arr))
print("Максимум:", np.max(arr))
print("Минимум:", np.min(arr))
