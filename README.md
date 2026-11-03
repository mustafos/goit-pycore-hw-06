# Homework 6. Class Basics

An address book for a future CLI assistant. Contacts are stored as objects: each one has a required name and a list of phone numbers.

The solution is in [`task1.py`](task1.py).

## Run

Python 3 is required. No extra libraries are needed.

```bash
python3 task1.py
```

The script creates a book, adds John and Jane, changes John's phone, looks up his second number, and deletes Jane. Expected output:

```text
Contact name: John, phones: 1234567890; 5555555555
Contact name: Jane, phones: 9876543210
Contact name: John, phones: 1112223333; 5555555555
John: 5555555555
```

Importing the classes does not run the example.

## Classes

| Class | Purpose |
| --- | --- |
| `Field` | Base field of a contact record |
| `Name` | Contact name, required |
| `Phone` | Phone number with format validation |
| `Record` | One contact: a name and a list of phones |
| `AddressBook` | Contact book based on `UserDict` |

### Record

- `add_phone(phone)` adds a number.
- `find_phone(phone)` returns a `Phone` object or `None`.
- `edit_phone(old_phone, new_phone)` replaces a number.
- `remove_phone(phone)` removes a number.

### AddressBook

- `add_record(record)` stores the record in `self.data` by name.
- `find(name)` returns the record or `None`.
- `delete(name)` removes the record by name.

## Validation

- A name must be a non-empty string. Leading and trailing spaces are removed.
- A phone number must be a string of exactly 10 digits.
- Editing or removing a missing phone, and deleting a missing contact, raises `ValueError`.
- If the new number is invalid during an edit, the old number stays unchanged.
