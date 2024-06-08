
import os

# Define a dictionary to store contacts
contacts = {}

# Function to load contacts from file
def load_contacts():
    global contacts
    if os.path.exists("contacts.txt"):
        with open("contacts.txt", "r") as file:
            for line in file:
                name, email, phone = line.strip().split(",")
                contacts[name] = (email, phone)

# Function to save contacts to file
def save_contacts():
    with open("contacts.txt", "w") as file:
        for name, (email, phone) in contacts.items():
            file.write(f"{name},{email},{phone}\n")

# Function to add a new contact
def add_contact():
    name = input("Enter name: ")
    email = input("Enter email: ")
    phone = input("Enter phone number: ")
    contacts[name] = (email, phone)
    print("Contact added successfully.")
    save_contacts()

# Function to list all contacts
def list_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for name, (email, phone) in contacts.items():
            print(f"Name: {name}, Email: {email}, Phone: {phone}")

# Function to delete a contact
def delete_contact():
    name = input("Enter name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
        save_contacts()
    else:
        print("Contact not found.")

# Load contacts from file
load_contacts()

# Main loop
while True:
    print("\n")
    print("\t   ___________________________")
    print("\t  | CONTACT MANAGEMENT SYSTEM |")
    print("\t  |___________________________|")
    print("\t  |1.| Add Contact            |")
    print("\t  |2.| List Contacts          |")
    print("\t  |3.| Delete Contact         |")
    print("\t  |4.| Exit                   |")
    print("\t  |__|________________________|")
    print("\n")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        add_contact()
    elif choice == 2:
        list_contacts()
    elif choice == 3:
        delete_contact()
    elif choice == 4:
        break
    else:
        print("Invalid choice. Try again.")        
   