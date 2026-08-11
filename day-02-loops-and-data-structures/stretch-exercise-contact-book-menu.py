"""
Exercise: Contact Book Menu
Student: Dristi Bhattarai
Day: 2
"""
contacts = {}

while True:
    print("\nContact Book")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. Display all contacts")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # 1. Add contact
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")

        contacts[name] = {
            "phone": phone,
            "email": email
        }

        print("Contact added successfully.")

    # 2. Search contact
    elif choice == "2":
        name = input("Enter name to search: ")

        if name in contacts:
            print("Name:", name)
            print("Phone:", contacts[name]["phone"])
            print("Email:", contacts[name]["email"])
        else:
            print("Contact not found.")

    # 3. Delete contact
    elif choice == "3":
        name = input("Enter name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    # 4. Display all contacts
    elif choice == "4":
        if contacts:
            for name, details in contacts.items():
                print("\nName:", name)
                print("Phone:", details["phone"])
                print("Email:", details["email"])
        else:
            print("No contacts available.")

    # 5. Exit
    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")