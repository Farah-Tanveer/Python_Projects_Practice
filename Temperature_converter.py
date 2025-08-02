while True:
    print("====Choose an option====")
    print("1.Celsius to Fahrenheit")
    print("2.Fahrenheit to Celsius")
    print("3.Celsius to Kelvin")
    print("4.Kelvin to Celsius")
    print("5.Fahrenheit to Kelvin")
    print("6.Kelvin to Fahrenheit")
    print("7.Exit")
    choice=0
    c=f=k=0
    try:
        choice=int(input("Enter your choice:"))
        match choice:
            case 1:
                c=float(input("Enter temperature:"))
                print(f"{c}°C = {((c * 9/5) + 32):.2f}°F")
            case 2:
                f=float(input("Enter temperature:"))
                print(f"{f}°F = {((f - 32) * 5/9):.2f}°C")
            case 3:
                c=float(input("Enter temperature:"))
                print(f"{c}°C = {(c + 273.15):.2f}K")
            case 4:
                k=float(input("Enter temperature:"))
                print(f"{k}K = {(k-273.15):.2f}°C")
            case 5:
                f=float(input("Enter temperature:"))
                print(f"{f}°F = {((f - 32) * 5/9 + 273.15):.2f}K")
            case 6:
                k=float(input("Enter temperature:"))
                print(f"{k}K = {((k - 273.15) * 9/5 + 32):.2f}°F")
            case 7:
                print("Thanks for using the temperature converter!")
                break
            case _:
                print("Invalid choice. Choose valid one.")
    except ValueError:
        print("Please enter a number between 1-7.")
