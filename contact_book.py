class Contact():
    
    def __init__(self,StoreName,PhoneNo,Email,Address):
        self.StoreName=StoreName
        self.PhoneNo=PhoneNo
        self.Email=Email
        self.Address=Address
        
class ContactBook():

    def __init__(self):
        self.Contact=[]
        
    def add_contact(self,StoreName,PhoneNo,Email,Address):
        new_contact=Contact(StoreName,PhoneNo,Email,Address)
        self.Contact.append(new_contact)
        print(f"Contact'{StoreName}'added successfully")
        
    def view_contact(self):
        if not self.Contact:
            print("No Contact Available")
            return
        print("Contact List:")
        for Contact in self.Contact:
            print(f"\nContact Name-{Contact.StoreName}\nPhoneNo-{Contact.PhoneNo}\nEmail-{Contact.Email}\nAddress-{Contact.Address}\n")
            
    def search_contact(self,query):
        found_Contact=[c for c in self.Contact if query.lower() in c.StoreName.lower() or query in c.PhoneNo]
        if found_Contact:
            print("Search results:")
            for Contact in found_Contact:
                print(f"Contact Name-{Contact.StoreName}\nPhoneNo-{Contact.PhoneNo}\n")
        else:
            print("No Contacts found")
            
    def update_contact(self,StoreName,new_StoreName=None,new_PhoneNo=None,new_Email=None,new_Address=None):
        for Contact in self.Contact:
            if Contact.StoreName==StoreName:
                Contact.StoreName=new_StoreName
                print("contact{StoreName}Updated Successfully")
                return
            print(f"Contact'{StoreName}'not found")
            
    def delete_contact(self,StoreName):
        for i,Contact in enumerate(self.Contact):
            if(Contact.StoreName==StoreName):
                del self.Contact[i]
                print(f"{StoreName}deleted successfully")
                return
            print("Contact{StoreName}not found")
            
def main():
        contact_book=ContactBook()

        while True:
            
            print("-- Contact Book Menu --")
            print("1. Add Contact")
            print("2. View Contact")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")
         
            choice = input("Choose an option: ")
    
            if choice == '1':
                StoreName = input("Enter the Name of the Contact: ")
                PhoneNo = input("Enter the PhoneNo of the contact: ")
                Email = input("Enter the Email of the contact: ")
                Address = input("Enter the Address of the Contact: ")
                contact_book.add_contact(StoreName, PhoneNo, Email, Address)
                
            elif choice == '2':
                contact_book.view_contact()
                
            elif choice == '3':
                query = input("Enter StoreName or PhoneNo to be searched: ")
                contact_book.search_contact(query)
                
            elif choice == '4':
                StoreName = input("Enter the StoreName to Update: ")
                new_StoreName = input("New StoreName: ")
                new_PhoneNo = input("New PhoneNo: ")
                new_Email = input("New Email: ")
                new_Address = input("New Address: ")
                contact_book.update_contact(StoreName, new_StoreName or None, new_PhoneNo or None, new_Email or None, new_Address or None)
                
            elif choice == '5':
                StoreName = input("Enter the StoreName to delete: ")
                contact_book.delete_contact(StoreName)
                
            elif choice == '6':
                print("Exiting the contact book.")
                break
            
            else:
                print("Invalid Option, Please Try Again")

if __name__=="__main__":
    main()
                
           
    
