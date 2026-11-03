from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty")

        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must contain exactly 10 digits")

        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def find_phone(self, phone):
        for item in self.phones:
            if item.value == phone:
                return item

        return None

    def remove_phone(self, phone):
        found_phone = self.find_phone(phone)

        if found_phone:
            self.phones.remove(found_phone)
            return True

        return False

    def edit_phone(self, old_phone, new_phone):
        found_phone = self.find_phone(old_phone)

        if found_phone is None:
            raise ValueError("Phone number not found")

        new_phone = Phone(new_phone)

        index = self.phones.index(found_phone)
        self.phones[index] = new_phone

    def __str__(self):
        phones = "; ".join(phone.value for phone in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

book = AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")

book.add_record(jane_record)

# Display all contacts
for name, record in book.data.items():
    print(record)

# Find and edit John's phone
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)

# Find a specific phone
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")

# Delete Jane
book.delete("Jane")

print("\nAfter deleting Jane:")
for record in book.data.values():
    print(record)