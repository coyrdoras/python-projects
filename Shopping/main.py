shopping_list = []

def add_list(add):
    shopping_list.append(add)

def remove_list(remove):
    if remove in shopping_list:
        shopping_list.remove(remove)
    else:
        print("\nListde bu mehsul onsuzda yox idi!")

def show_list():
    if shopping_list:
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}")
    else:
        print("Siyahi boşdur!")

while True:
    print("\n1. Add to List")
    print("2. Remove from List")
    print("3. Show the List")
    print("4. Exit\n")

    choice = input("Choice: ")

    if choice == "1":
        a = input("Elave edilecek mehsul: ")
        add_list(a)

    elif choice == "2":
        b = input("Silinecek mehsul: ")
        remove_list(b)

    elif choice == "3":
        show_list()
    else:
        break