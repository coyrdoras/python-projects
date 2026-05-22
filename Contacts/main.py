import json

try:
    with open("contacts.json", "r") as f:
        contacts = json.load(f)
except FileNotFoundError:
    contacts = {}  # fayl yoxdursa boş dictionary

def add():
    name = input("Name: ")
    
    while True:
        try:
            phone = int(input("Phone: "))
            break
        except ValueError:
            print("\nPlease use numbers! Try again!\n")

    email = input("Email: ")
    if "@" not in email:
        while "@" not in email:
                print("\n'@' is not in the email! Try again!\n")
                email = input("Email: ")

    contacts[name] = {"phone": phone, "email": email}
    
    with open("contacts.json", "w") as f:
        json.dump(contacts, f)

    print("\nContact was added!")

def search():
    name = input("\n Input contact's name: ")
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]["phone"]}")
        print(f"Email: {contacts[name]["email"]}")
    else:
        print("\nThere is no such contact in Contacts!\n")

def delete():
    name = input("\nInput contact's name: ")       
    if name in contacts:
        del contacts[name]

        with open("contacts.json", "w") as f:
            json.dump(contacts, f)

        print(f"{name} silindi!")
    else:
        print("\nThere is no contact in Contacts")

def show():
    if contacts:
        for name, contact in contacts.items():
            print(f"\nName: {name}")
            print(f"Phone: {contact["phone"]}")
            print(f"Email: {contact["email"]}")
    else:
        print("\nContacts list is empty!\n")

while True:
    print('''
1. Add to Contacts
2. Search in Contacts
3. Delete existing Contacts
4. Show Contacts List\n''')
    
    choice = input("Choice: ")
    
    if choice == "1":
        add()

    elif choice == "2":
        search()
    
    elif choice == "3":
        delete()

    elif choice == "4":
        show()

    else:
        print("Please choose a variant between 1-4")