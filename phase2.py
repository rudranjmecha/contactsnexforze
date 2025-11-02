CONTACTS = []
def display_menu():
    print("\n==============================")
    print("📞 Welcome to contacts manager")
    print("==============================")
    print("1. Add New Contact")
    print("2. View All Contacts")
    print("3. Exit Application")
    print("------------------------------")

def add_new_contact():
    print("\n--- Add New Contact ---")
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email Address: ")

    new_contact = {
        'name': name,
        'phone': phone,
        'email': email
    }
    
    CONTACTS.append(new_contact)
    
    print(f"\n Contact '{name}' added successfully!")

def view_all_contacts():
    """Displays all contacts stored in the CONTACTS list."""
    print("\n--- All Saved Contacts ---")
    
    if not CONTACTS:
        print("Your contact list is currently empty.")
        return 
    
    for index, contact in enumerate(CONTACTS):
        print(f"\nContact #{index + 1}:")
        print(f"  Name:  {contact['name']}")
        print(f"  Phone: {contact['phone']}")
        print(f"  Email: {contact['email']}")
    
    print("--------------------------")


def main():
    running = True 
    while running:
        display_menu()
        choice = input("Enter your choice (1, 2, or 3): ").strip()

        if choice == '1':
            add_new_contact() 

        elif choice == '2':
            view_all_contacts() 

        elif choice == '3':
            print("\n Thank you for using the Contacts Manager!Have a great day.")
            running = False
            
        else:
            print("\n🚨 Invalid selection. Please enter between 1, 2, or 3.")

if __name__ == "__main__":
    main()