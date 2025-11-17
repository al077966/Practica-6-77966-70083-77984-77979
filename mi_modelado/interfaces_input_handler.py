def pedir_numero(prompt):
    while True:
        try:
            val = float(input(prompt))
            if val <= 0: raise ValueError
            return val
        except ValueError:
            print("Ingresa un número válido mayor a 0.")

def pedir_entero(prompt):
    while True:
        try:
            val = int(input(prompt))
            if val <= 0: raise ValueError
            return val
        except ValueError:
            print("Ingresa un número entero válido.")
