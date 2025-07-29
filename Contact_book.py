contacts = {}
file = open("data.txt", "r")
data = file.read().strip().split(",")
file.close()
i = 0
while i < len(data) - 1:
    name = data[i]
    phone = data[i + 1]
    contacts[name] = phone
    i += 2

while True:
    print("====Choose an option====")
    print("1.Save Contact")
    print("2.Delete Contact")
    print("3.Find Contact")
    print("4.Exit")
    choice=0
    choice=int(input("Enter your choice:"))
    match choice:
        case 1:
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            contacts[name] = phone
            file = open("data.txt", "w")
            for n, p in contacts.items():
                file.write(f"{n},{p},")
            file.close()
            print(f"Contact saved for {name}.")
        case 2:
            name = input("Enter name to delete: ")
            if name in contacts:
                del contacts[name]
                file = open("data.txt", "w")
                for n, p in contacts.items():
                    file.write(f"{n},{p},")
                file.close()
                print(f"Contact deleted for {name}.")
            else:
                print("Contact not found.")
        case 3:
            name = input("Enter name to find: ")
            if name in contacts:
                print(f"Phone number of {name} is {contacts[name]}.")
            else:
                print("Contact not found.")
        case 4:
            print("Thanks for using....")
            break
        case _:
             print("Invalid choice. Please enter a number from 1 to 4.")            

    
    
    