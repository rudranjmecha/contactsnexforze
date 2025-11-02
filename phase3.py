CONTACTS = []

def get_valid_phone():
    while True:
        phone = input("Enter Phone Number (Digits only): ").strip()
        if phone.isdigit():
            return phone
        else:
            print("Phone number must contain only digits.Enter digits only.")
def display_menu():
    print("\n==============================")
    print("Contact Manager Main Menu")
    print("==============================")
    print("1. Add New Contact")
    print("2. View All Contacts")
    print("3. Exit Application")
    print("------------------------------")

def add_new_contact():
    print("\n--- Add New Contact ---")
    
    name = input("Enter Name: ").strip()
    email = input("Enter Email Address: ").strip()
    
    phone = get_valid_phone() 
    
    new_contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    
    CONTACTS.append(new_contact)
    
    print(f"\n Contact '{name}' added successfully!")

def view_all_contacts():
    """Nicely formats and displays the details from each contact dictionary."""
    print("\n--- All Saved Contacts ---")
    
    if not CONTACTS:
        print("Your contact list is currently empty.")
        return
    
    # Print a header for clean formatting
    print(f"{'#':<3} | {'Name':<20} | {'Phone':<15} | {'Email'}")
    print("-" * 60)

    for index, contact in enumerate(CONTACTS):

        print(
            f"{index + 1:<3} | " 
            f"{contact['name']:<20} | "
            f"{contact['phone']:<15} | "
            f"{contact['email']}"
        )
    
    print("-" * 60)

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
            print("\n Thank you for using the Contact Manager! Have a great day.")
            running = False
            
        else:
            print("\n Invalid choice. Please enter between 1, 2, or 3.")
            
if __name__ == "__main__":
    main()