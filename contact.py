import json
import os

CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return []

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Display all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    print("\nContact List:")
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. {contact['name']} | {contact['phone']} | {contact['email']}")

# Add a new contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("Contact added successfully!")

# Edit a contact
def edit_contact(contacts):
    view_contacts(contacts)
    try:
        index = int(input("Enter the number of the contact to edit: ")) - 1
        if 0 <= index < len(contacts):
            print("Leave a field blank to keep it unchanged.")
            name = input(f"New name [{contacts[index]['name']}]: ") or contacts[index]['name']
            phone = input(f"New phone [{contacts[index]['phone']}]: ") or contacts[index]['phone']
            email = input(f"New email [{contacts[index]['email']}]: ") or contacts[index]['email']
            contacts[index] = {"name": name, "phone": phone, "email": email}
            save_contacts(contacts)
            print("Contact updated successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete a contact
def delete_contact(contacts):
    view_contacts(contacts)
    try:
        index = int(input("Enter the number of the contact to delete: ")) - 1
        if 0 <= index < len(contacts):
            deleted = contacts.pop(index)
            save_contacts(contacts)
            print(f"Deleted contact: {deleted['name']}")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")

# Main menu loop
def main():
    contacts = load_contacts()
    while True:
        print("\n--- Contact Manager ---")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()
        if choice == "1":
            view_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Exiting Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
