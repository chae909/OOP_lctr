class ContactList(list["Contact"]):
    def search(self, name:str)->list["Contact"]:
        matching_contacts: list["Contact"] = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts

class Contact:
    all_contacts = ContactList()

    def __init__(self, name:str, email:str) -> None:
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def __repr__(self) -> str:
        return f"Name: {self.name}, Email: {self.email}"

if __name__ == "__main__":
    contacts = [Contact("A. John", "johna@example.com"),
                Contact("B. John", "johnb@sloop.net"),
                Contact("C. Jenny", "cutty@sack.io")]

    search_result = [c for c in Contact.all_contacts.search("John")]
    for customer in search_result:
        print(customer)