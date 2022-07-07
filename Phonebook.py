class Phonebook:
    def __init__(self):
        while True:
            print("Choose an option:")
            print("1. Insert a contact.")
            print("2. Update a contact.")
            print("3. Delete a contact.")
            print("4. Search a contact.")
            print("5. Display")
            print("6. Exit")

            choice = int(input("Enter a number(1-6) to begin:"))

            if choice == 1:
                self.insert()
            elif choice == 2:
                self.update()
            elif choice == 3:
                self.delete()
            elif choice == 4:
                self.search()
            elif choice == 5:
                self.display()
            else:
                break

    def insert(self):
        while True:
            try:

                name = input("Name:")
                phoneNo = input("Phone No:")
                address = input("Address:")
                email = input("Email:")

                with open("phonebook.txt", 'a') as file_object:
                    file_object.write(f"Name:{name} , Phone number: {phoneNo} , Address: {address} , Email: {email}\n")
                    file_object.write(f"-----------------------------------------------------------------------------\n")

                break
            except:
                print("Unexpected error!")
                break

    def update(self):
        with open("phonebook.txt", 'r+') as file_object:
            search = input("Name you want to update:")
            str = ' '
            while(str):
                str = file_object.readline()
                linelist = str.split(" , ")
                if len(str)> 0:
                    if linelist[0] == "Name:"+search:
                        name = input("Name:")
                        phoneNo = input("Phone No:")
                        address = input("Address:")
                        email = input("Email:")
                        file_object.write(f"Name:{name} , Phone number: {phoneNo} , Address: {address} , Email: {email}\n")


            else:
                print("No data found")

    def delete(self):
        with open('phonebook.txt', 'r') as file_object:
            lines = file_object.readlines()

            search = input("Enter a contact you want to delete:")

            with open('phonebook.txt', 'w') as file_object:
                for line in lines:
                    if line.find(f"{search}") == -1:
                        file_object.write(line)
        print("Deleted")

    def search(self):
        with open("phonebook.txt", 'r') as file_object:
            search = input("Name you want to search:")
            for i in file_object:
                if search in i:
                    print(i)

    def display(self):
        with open("phonebook.txt", 'r') as file_object:
            phbook = file_object.read()
        print(phbook)



test = Phonebook()