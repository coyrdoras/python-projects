class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []

accounts = {}

def create_account(name, balance=0):
    accounts[name] = BankAccount(name, balance)
    print(f"{name} üçün hesab açildi!")

def deposit(name, amount):
    accounts[name].balance += amount
    accounts[name].history.append(f"+{amount} yatirildi")
    print(f"{amount} yatirildi. Balans: {accounts[name].balance}")

def withdraw(name, amount):
    if accounts[name].balance >= amount:
        accounts[name].balance -= amount
        accounts[name].history.append(f"-{amount} çəkildi")
        print(f"{amount} çəkildi. Balans: {accounts[name].balance}")
    else:
        print("Balans kifayət deyil!")

def transfer(from_name, to_name, amount):
    if from_name not in accounts or to_name not in accounts:
        print("Hesab tapilmadi!")
    elif accounts[from_name].balance < amount:
        print("Balans kifayət deyil!")
    else:
        accounts[from_name].balance -= amount
        accounts[to_name].balance += amount
        accounts[from_name].history.append(f"-{amount} → {to_name}ə köçürüldü")
        accounts[to_name].history.append(f"+{amount} ← {from_name}dən gəldi")
        print(f"{amount} köçürüldü!")

while True:
    print("\n1. Hesab aç\n2. Balans\n3. Yatir\n4. Çək\n5. Tarixçə\n6. Köçür\n7. Çix")
    choice = input("Seçim: ")

    if choice == "1":
        name = input("Ad: ")
        balance = int(input("İlkin balans: "))
        create_account(name, balance)

    elif choice == "2":
        name = input("Ad: ")
        if name in accounts:
            print(f"Balans: {accounts[name].balance}")
        else:
            print("Hesab tapilmadi!")

    elif choice == "3":
        name = input("Ad: ")
        if name in accounts:
            try:
                amount = int(input("Məbləğ: "))
            except ValueError:
                print("Rəqəm daxil edin!")
                continue
            deposit(name, amount)
        else:
            print("Hesab tapilmadi!")

    elif choice == "4":
        name = input("Ad: ")
        if name in accounts:
            amount = int(input("Məbləğ: "))
            withdraw(name, amount)
        else:
            print("Hesab tapilmadi!")

    elif choice == "5":
        name = input("Ad: ")
        if name in accounts:
            print(accounts[name].history)
        else:
            print("Hesab tapilmadi!")

    elif choice == "6":
        from_name = input("Kimdən: ")
        to_name = input("Kimə: ")
        amount = int(input("Məbləğ: "))
        transfer(from_name, to_name, amount)

    elif choice == "7":
        break
















'''

            MENIM SEHV KODUM!!!

'''

'''class Bank_account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

john = Bank_account(owner="John", balance=503)
jake = Bank_account(owner="Jake", balance=1234)
tom = Bank_account(owner="Tom", balance=67)
tim = Bank_account(owner="Tim", balance=12834)

def depositt():
    name = input("Write your account name: ")
    if name in john.owner:
        amount = input("Input amount of deposite: ")
        amount = int(amount)
        john.balance += amount
        print("Deposit successfully!")
    else:
        print("Account name is wrong! Try new one or creat a new account!")

def withdraw():
    name = input("Write your account name: ")
    if name in john.owner:
        amount = input("Input amount of withdraw: ")
        amount = int(amount)
        if amount > john.balance:
            print("Insufficient funds!")
        else:
            john.balance -= amount
            print("Withdraw successfully!")
    else:
        print("Account name is wrong! Try new one or creat a new account!")

def check():'''
