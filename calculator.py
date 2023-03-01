number_1 = input("Enter number 1: ")
number_2 = input("Enter number 2: ")
print("1. Dodaj")
print("2. Odejmij")
print("3. Pomnóż")
print("4. Podziel")
print("5. Wyjdź")
choice = input("Wybierz numer operacji: ")
if choice == '1':
    result = number_1 + number_2
    print(number_1, "+", number_2, "=", result)
elif choice == '2':
    result = number_1 - number_2
    print(number_1, "-", number_2, "=", result)
elif choice == '3':
    result = number_1 * num2
    print(number_1, "*", number_2, "=", result)
elif choice == '4':
    result = number_1 / num2
    print(number_1, "/", number_2, "=", result)
elif choice == '5':
    print("Do widzenia!")
else:
    print("Nieprawidłowy wybór. Spróbuj ponownie.")
