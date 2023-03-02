while True:
    number_1 = input("Enter number 1: ")
    number_2 = input("Enter number 2: ")
    try:
        num1 = float(number_1)
        num2 = float(number_2)
    except ValueError:
        print("Nieprawidłowe dane. Spróbuj ponownie.")
        continue
    print("1. Dodaj")
    print("2. Odejmij")
    print("3. Pomnóż")
    print("4. Podziel")
    print("5. Wyjdź")
    choice = input("What do you want to do: ")
    if choice == '1':
        result = num1 + num2
        print(num1, "+", num2, "=", result)
    elif choice == '2':
        result = num1 - num2
        print(num1, "-", num2, "=", result)
    elif choice == '3':
        result = num1 * num2
        print(num1, "*", num2, "=", result)
    elif choice == '4':
        if num2 == 0:
            print("We can't divide by 0.")
        else:
            result = num1 / num2
            print(num1, "/", num2, "=", result)
    elif choice == '5':
        print("Goodbye")
        break
    else:
        print("Something went wrong. Try again.")
