print("1.Celsius to Fahrenheit.")
print("2.Fahrenheit to Celsius.")
Choice = int(input("Which temperature unit would you need to change?"))
match Choice:
    case 1:
        Celsius = float(input("Enter the temprature in celsius:"))
        Fahrenheit = (Celsius * 9/5) + 32
        print(f"The temprature in Fahrenheit is {Fahrenheit}°F")
    case 2:
        Fahrenheit = float(input("Emter the tempature in Fahrenheit:"))
        Celsius =(Fahrenheit -32) *5/9
        print(f"The temprature in celsius in {Celsius}°C")
    case _:
        print("Invalid Choice.Please select either 1 or 2.")
