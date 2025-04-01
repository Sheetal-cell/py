class ContactBook:
    def __init__(self):
        self.contacts = {}
    
    def add_contact(self, name, phone):
        self.contacts[name] = phone
        print(f"Added: {name} - {phone}")
    
    def display_contacts(self):
        print("\nContacts:")
        for name, phone in self.contacts.items():
            print(f"{name}: {phone}") if self.contacts else print("No contacts found.")
    
    def search_contact(self, name):
        print(f"{name}: {self.contacts.get(name, 'Not found')}")

book = ContactBook()

while (choice := input("\n1. Add  2. Show  3. Search  4. Exit\nChoose: ")) != '4':
    if choice == '1': book.add_contact(input("Name: "), input("Phone: "))
    elif choice == '2': book.display_contacts()
    elif choice == '3': book.search_contact(input("Name: "))
    else: print("Invalid choice.")

print("Goodbye!")
