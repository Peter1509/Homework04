# Diverse Imports
import calculations

print("="*50)
print("Willkommen bei Deinem persönlichen Taschenrechner.")
print("Du kannst so viele Berechnungen durchführungen wie Du willst")
print("Wenn Du das Programm beenden willst, bestätige den Operator ohne Eingabe mit ENTER.")
print("="*50)


while True:
    try:

# Verhalten bei diverser Eingabe


        print("Wähle eine Rechenart aus!")
        print("------- [ + , - , * , / , Quadrat , Wurzel , Log ] -------")
        operator= input("Rechenart auswhälen: ").strip().lower()

        if operator == "":
            operator = input("Willst Du wirklich das Programm beenden? Bestätige mit ENTER:").strip().lower()

            if operator == "":
                break

        elif operator in ["+", "-", "/", "*"]:
            number1 = int(input("Erste Zahl eingeben: ").strip())
            number2 = int(input("Zweite Zahl eingeben: ").strip())

        elif operator in ["quadrat", "wurzel", "log"]:
            number1 = int(input("Zahl eingeben: ").strip())


        # Berechnung
        if operator == "+":
            result = calculations.addition(number1, number2)
            print("Ergebis: " + str(result))
            calculations.into_file("Berechnung: " + str(number1) + " " + operator + " " + str(number2) + " = " + str(result))
        elif operator == "-":
            result = calculations.subtraction(number1, number2)
            print("Ergebis: " + str(result))
            calculations.into_file("Berechnung: " + str(number1) + " " + operator + " " + str(number2) + " = " + str(result))
        elif operator == "*":
            result = calculations.multiplication(number1, number2)
            print("Ergebis: " + str(result))
            calculations.into_file("Berechnung: " + str(number1) + " " + operator + " " + str(number2) + " = " + str(result))
        elif operator == "/":
            result = calculations.division(number1, number2)
            print("Ergebis: " + str(result))
            calculations.into_file("Berechnung: " + str(number1) + " " + operator + " " + str(number2) + " = " + str(result))
        elif operator == "quadrat":
            result = calculations.square(number1)
            print("Ergebis: " + str(result))
            calculations.into_file("Berechnung: " + operator + " von " + str(number1) + " = " + str(result))
        elif operator == "wurzel":
            result = calculations.root(number1)
            print("Ergebis: " + str(result))
            calculations.into_file("Berechnung: " + operator + " von " + str(number1) + " = " + str(result))
        elif operator == "log":
            result = calculations.logarithm(number1)
            print("Ergebis: " + str(result))
            calculations.into_file("Berechnung: " + operator + " von " + str(number1) + " = " + str(result))




    except Exception as e:
        print()
        print("Error:")
        print(e)
        print("Bitte erneut versuchen")
        print()

print("Programm beendet!")