
import uuid
from contact import Contact

class PhoneBook:

    def __init__(self):
        self.contacts = {}
        self.deleted = []

    def add_contact(self, contact):
        self.contacts[contact.id] = contact
        print("Contact added successfully.")

    def find_contact_by_id(self, contact_id):
        return self.contacts.get(contact_id, None)

    def find_contacts_by_lastname(self, last_name):
        return [contact for contact in self.contacts.values() if contact.last_name == last_name]

    def remove_contact(self, contact_id):
        if contact_id in self.contacts:
            removed_contact = self.contacts.pop(contact_id)
            self.deleted.append(removed_contact)
            print("Contact removed successfully.")
            return True
        else:
            print("Contact not found.")
            return False

    def restore_contact(self, contact_id):
        for deleted_contact in self.deleted:
            if deleted_contact.id == contact_id:
                self.contacts[contact_id] = deleted_contact
                self.deleted.remove(deleted_contact)
                print("Contact restored successfully.")
                return True
        print("Contact not found in deleted contacts.")
        return False

    def add_phone_number(self, contact_id):
        contact = self.contacts.get(contact_id, None)
        if contact:
            new_number = input("\nEnter a new phone number: ")
            contact.phone_number = contact.validate_phone_number(new_number)
            print("Phone number added successfully.")
            return True
        else:
            print("Contact not found.")
            return False
            
    def group_by_city(self, city):
        count = sum(1 for contact in self.contacts.values() if contact.city == city)
        return {city: count}
        
