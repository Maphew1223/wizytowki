from faker import Faker
fake = Faker(['pl_PL'])

class BaseContact:

    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    def contact(self):
        print(f"Wybieram numer {self.phone_number} i dzwonię do {self.first_name} {self.last_name}.")

    @property
    def label_length(self):
        return len(self.first_name) + len(self.last_name) + 1

class BusinessContact(BaseContact):


    def __init__(self, position, company, work_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company = company
        self.work_phone = work_phone

    def contact(self):
        print(f"Wybieram numer {self.work_phone} i dzwonię do {self.first_name} {self.last_name}.")

    @property
    def label_length(self):
        return len(self.first_name) + len(self.last_name) + 1

def create_contacts(contact_type, quantity):
    contacts = []
    for i in range(quantity):
        if contact_type == "base":
            contacts.append(BaseContact(
                first_name = fake.first_name(),
                last_name = fake.last_name(),
                phone_number = f"+48 {fake.numerify('### ### ###')}",
                email = fake.email()
            ))
        elif contact_type == "business":
            contacts.append(BusinessContact(
                first_name = fake.first_name(),
                last_name = fake.last_name(),
                phone_number = f"+48 {fake.numerify('### ### ###')}",
                email = fake.email(),
                position = fake.job(),
                company = fake.company(),
                work_phone = f"+48 {fake.numerify('### ### ###')}",   
            ))
    return contacts
            
base_contacts = create_contacts("base", 5)
business_contacts = create_contacts("business", 5)
print("Wizytówki bazowe:")
for contact in base_contacts:
    contact.contact()
    print(f"Długość etykiety: {contact.label_length}")
print("\nWizytówki firmowe:")
for contact in business_contacts:
    contact.contact()
    print(f"Długość etykiety: {contact.label_length}")