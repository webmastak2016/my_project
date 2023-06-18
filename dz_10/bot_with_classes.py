from collections import UserDict


class Field:
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone

    def __str__(self):
        result = f"Name: {self.name}\n"
        if self.phones:
            result += "Phones:\n"
            for phone in self.phones:
                result += f"- {phone}\n"
        return result


class AddressBook(UserDict):
    def add_record(self, record):
        if record.name.value in self.data:
            existing_record = self.data[record.name.value]
            existing_record.phones.extend(record.phones)
        else:
            self.data[record.name.value] = record

    def delete_record(self, name):
        del self.data[name]

    # def search_by_name(self, name):
    #     result = []
    #     for record in self.data.values():
    #         if record.name.value.lower() == name.lower():
    #             result.append(record)
    #     return result

    # def search_by_phone(self, phone):
    #     result = []
    #     for record in self.data.values():
    #         for p in record.phones:
    #             if p.value == phone:
    #                 result.append(record)
    #     return result


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            return str(e)
    return wrapper


address_book = AddressBook()


@input_error
def add_contact(name, phone):
    record = Record(name)
    record.add_phone(phone)
    address_book.add_record(record)
    return f"Contact '{name}' with phone '{phone}' has been added."


@input_error
def change_phone(name, old_phone, new_phone):
    if name not in address_book.data:
        return f"!!! Contact '{name}' does not exist !!!"
    record = address_book.data[name]
    record.edit_phone(old_phone, new_phone)
    return f"The phone number for contact '{name}' has been changed to '{new_phone}'."


@input_error
def remove_contact(name):
    if name not in address_book.data:
        return f"!!! Contact '{name}' does not exist !!!"
    address_book.delete_record(name)
    return f"Contact '{name}' has been removed."


@input_error
def get_phone(name):
    if name not in address_book.data:
        return f"Contact '{name}' does not exist."
    record = address_book.data[name]
    phones = ", ".join([str(phone) for phone in record.phones])
    return f"The phone number(s) for contact '{name}' is/are: {phones}"


def show_all_contacts():
    if not address_book.data:
        return "The contact list is empty."
    result = "Contacts:\n"
    for record in address_book.data.values():
        result += str(record) + "\n"
    return result


command_text = 'Hello, Add, Change, Remove, Phone, Search, Show all, Good bye, Close or Exit'


def main():
    print(f"Enter command: {command_text}")
    while True:
        command = input("Enter command > ").lower()
        if command == "hello":
            print(f"How can I help you?")
        elif command == "add":
            try:
                name = str(input("Enter Name > "))
                phone = int(input("Enter Phone > "))
                print(add_contact(name, phone))
            except ValueError:
                print("Invalid input. Name -> String. Phone -> Number")
        elif command == "change":
            try:
                name = input("Enter Name > ")
                old_phone = input("Enter Old Phone > ")
                new_phone = input("Enter New Phone > ")
                print(change_phone(name, old_phone, new_phone))
            except ValueError:
                print("Invalid input.")
        elif command == "remove":
            name = input("Enter Name > ")
            print(remove_contact(name))
        elif command == "phone":
            name = input("Enter Name > ")
            print(get_phone(name))
        # elif command == "search":
        #     inp = input("Enter Name or Phone > ")
        #     if inp.isnumeric():
        #         print(address_book.search_by_phone(int(inp)))
        #     else:
        #         print(address_book.search_by_name(inp))
        elif command == "show all":
            print(show_all_contacts())
        elif command == "good bye" or command == "close" or command == "exit":
            print("Good bye!")
            break
        else:
            print(
                f"Unknown command. Please try again. For example: {command_text}")


if __name__ == "__main__":
    main()
