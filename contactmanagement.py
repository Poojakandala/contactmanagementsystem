import json

FILE_NAME = "contacts.json"

def load_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_contacts():
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

contacts = load_contacts()

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts()
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    for i, c in enumerate(contacts, start=1):
        print(f"{i}. Name: {c['name']}, Phone: {c['phone']}, Email: {c['email']}")

def delete_contact():
    view_contacts()
    if not contacts:
        return
    index = int(input("Enter contact number to delete: ")) - 1
    if 0 <= index < len(contacts):
        contacts.pop(index)
        save_contacts()
        print("Contact deleted successfully!")

while True:
    print("\nContact Management System")
    choice = input("1. Add  2. View  3. Delete  4. Exit: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        break
