# main.py

def is_even(num):
    return num % 2 == 0
def is_positive(num):
    return num > 0
def is_multiple_of_5(num):
    return num % 5 == 0
def is_divisible_by_3_and_4(num):
    return num % 3 == 0 and num % 4 == 0

def main():
    while True:
        print("\n--- Clasificador de Números ---")
        print("1. Determinar si el número es par o impar.")
        print("2. Determinar si el número es positivo, negativo o cero.")
        print("3. Verificar si el número es múltiplo de 5.")
        print("4. Verificar si el número es divisible entre 3 y 4 al mismo tiempo.")
        print("5. Salir.")
        
        choice = input("Selecciona una opción (1-5): ")
        
        if choice == '5':
            print("Saliendo del programa.")
            break
        
        try:
            number = float(input("Ingresa el número que deseas analizar: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue
        
        if choice == '1':
            result = "par" if is_even(number) else "impar"
            print(f"El número {number} es {result}.")
        elif choice == '2':
            if number > 0:
                print(f"El número {number} es positivo.")
            elif number < 0:
                print(f"El número {number} es negativo.")
            else:
                print("El número es cero.")
        elif choice == '3':
            if is_multiple_of_5(number):
                print(f"El número {number} es múltiplo de 5.")
            else:
                print(f"El número {number} no es múltiplo de 5.")
        elif choice == '4':
            if is_divisible_by_3_and_4(number):
                print(f"El número {number} es divisible entre 3 y 4.")
            else:
                print(f"El número {number} no es divisible entre 3 y 4.")
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 5.")

if __name__ == "__main__":
    main()