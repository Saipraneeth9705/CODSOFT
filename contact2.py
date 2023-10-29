contact_book = []
while True:
    print("\nContact Book")
    print("1. Add Contact\n 2.View contact\n 3.Update contact\n 4.Delete contact\n 5.Quit\n ")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = str(input("Enter Name: "))
        phone = int(input("Enter Phone: "))
        email = input("Enter Email: ")
        address=input("enter Address:")
        contact = {"Name": name, "Phone": phone, "Email": email,"Address":address}
        contact_book.append(contact)
        print("Contact added successfully.")
    elif choice == "2":
        if not contact_book:
            print("No contacts found.")
        else:
            print("Contacts:")
            for i, contact in enumerate(contact_book, 1):
                print(f"{i}. Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}, Address:{contact['Address']}")
    elif choice == "3":
            index = int(input("Enter the index of the contact you want to update:"))
            name=input("enter the name of the contact to update:")
            for contact in contact_book:
              if contact['Name']==name:
                      new_name=input("enter the name:" )
                      contact['Name']=new_name
                      print("contact updated:")
            phone=input("enter the phone of the contact to update:")          
            for contact in contact_book:
                if contact['Phone']==phone:
                      new_phone=input("enter the phone:" )
                      contact['Phone']=new_phone
                      print("contact updated:")
            email=input("enter the email of the contact to update:")
            for contact in contact_book:
              if contact['Email']==email:
                      new_email=input("enter the email:" )
                      contact['Email']=new_email
                      print("contact updated:")
            ame=input("enter the name of the contact to update:")
            for contact in contact_book:
              if contact['Address']==address:
                      new_adress=input("enter the name:" )
                      contact['Name']=new_adress
                      print("contact updated:")

            for contact in contact_book:
              if contact['Name']==name:
                      new_name=input("enter the name:" )
                      contact['Name']=new_name
                      print("contact updated:")
    elif choice == "4":
        if not contact_book:
            print("No contact found. and try again later")
        else:
            print("Contacts:")
            for i, contact in enumerate(contact_book, 1):
                                print(f"{i}. Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}, Address:{contact['Address']}")

            index = int(input("Enter the index of the contact you want to delete: "))
            if 0 < index <= len(contact_book):
                deleted_contact = contact_book.pop(index - 1)
                print(f"Contact deleted: {deleted_contact['Name']}")
            else:
                print("Invalid index.")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice and Please try again.")
