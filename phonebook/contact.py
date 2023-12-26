import uuid

class Contact:

    cities = ["Ramlah", "Rahat", "Lod", "Jaffa", "kafr-kasem", "Taybe", "Tireh", "Um alfahm", "Alnasrah", "Hifa"]

    def __init__(self, first_name, last_name, phone_number, city):
        self.id = uuid.uuid4()
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = self.validate_phone_number(phone_number)
        self.city = self.validate_city(city)

    def validate_phone_number(self, phone_number):
        # Assuming the phone number should be in the format xx-xxxxxxx or xxx-xxxxxxx
        if len(phone_number) == 10 and phone_number[:2].isdigit() and phone_number[2] == '-' and phone_number[3:].isdigit():
            return phone_number
        elif len(phone_number) == 9 and phone_number.isdigit():
            return phone_number[:3] + '-' + phone_number[3:]
        else:
            raise ValueError("Invalid phone number format. Please use xx-xxxxxxx or xxx-xxxxxxx.")


    def validate_city(self, city):
        if city in self.cities:
            return city
        else:
            raise ValueError("Invalid city. Please choose from the provided list.")
         
    def __str__(self):
        return f"ID: {self.id}\nFirst Name: {self.first_name}\nLast Name: {self.last_name}\nPhone Number: {self.phone_number}\nCity: {self.city}"

