# Advanced Contact Book Application

import json
import os

FILE_NAME = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save contacts to file
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

# Generate next contact ID
def generate_id(contacts):
    if not contacts:
        return 1
    return max(contact["id"] for contact in contacts) + 1

# Add new contact
def add_contact(contacts):
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {
        "id": generate_id(contacts),
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully.")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    print("\nContact List:")
    for contact in contacts:
        print(f"""
ID: {contact['id']}
Name: {contact['name']}
Phone: {contact['phone']}
Email: {contact['email']}
Address: {contact['address']}
---------------------------""")

# Search contact by name or phone
def search_contact(contacts):
    search_value = input("Enter name or phone to search: ").lower()

    found = False
    for contact in contacts:
        if search_value in contact["name"].lower() or search_value in contact["phone"]:
            print(f"""
ID: {contact['id']}
Name: {contact['name']}
Phone: {contact['phone']}
Email: {contact['email']}
Address: {contact['address']}
---------------------------""")
            found = True

    if not found:
        print("Contact not found.")

# Update contact
def update_contact(contacts):
    try:
        contact_id = int(input("Enter Contact ID to update: "))
    except ValueError:
        print("Invalid ID.")
        return

    for contact in contacts:
        if contact["id"] == contact_id:
            contact["name"] = input("Enter new name: ")
            contact["phone"] = input("Enter new phone: ")
            contact["email"] = input("Enter new email: ")
            contact["address"] = input("Enter new address: ")

            save_contacts(contacts)
            print("Contact updated successfully.")
            return

    print("Contact not found.")

# Delete contact
def delete_contact(contacts):
    try:
        contact_id = int(input("Enter Contact ID to delete: "))
    except ValueError:
        print("Invalid ID.")
        return

    for contact in contacts:
        if contact["id"] == contact_id:
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted successfully.")
            return

    print("Contact not found.")

# Main program
def main():
    contacts = load_contacts()

    while True:
        print("""
-------- CONTACT BOOK MENU --------
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
------------------------------------
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()