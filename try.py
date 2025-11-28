try:
    a = float(input("Бірінші санды енгізіңіз: "))
    b = float(input("Екінші санды енгізіңіз: "))
    result = a / b
    print("нәтиже:", result)
except ZeroDivisionError:
    print("Нөлге бөлуге болмайды!")
except ValueError:
    print("Санды дұрыс енгізіңіз!")
