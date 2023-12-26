
from contact import Contact
from phonebook import PhoneBook
#  Example Usage
contact1 = Contact("Adam", "bahri", "12-4567890", "Lod")
contact2 = Contact("Sila", "emad", "98-7654320", "Lod")

phonebook = PhoneBook()
phonebook.add_contact(contact1)
phonebook.add_contact(contact2)

print("\nAll Contacts:")
for contact in phonebook.contacts.values():
    print(contact)

print("\nGroup by City:")
print(phonebook.group_by_city("Lod"))

phonebook.remove_contact(contact1.id)

print("\nAfter removing contact:")
for contact in phonebook.contacts.values():
    print(contact)
     