class Contact:
    all_contacts:list["Contact"] = []

    def __init__(self, name:str, email:str):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.email})"

#    def order(self, order: str):
#        print(f"If this were a real system, we would send '{order}' to {self.name}")

class Supplier(Contact):
    def order(self, order:str):
        print(f"If this were a real system, we would send '{order}' to {self.name}")


if __name__ == "__main__":
    c = Contact("Dusty", "dusty@example.com")
    s = Supplier("Steve", "steve@itmaybeahack.com")
    print(Contact.all_contacts)

    s.order("pliers")
    c.order("snacks")