def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            return str(e)
    return wrapper


contacts = {}


@input_error
def add_contact(name, phone):
    print('Enter Name & Phone')
    contacts[name] = phone
    return f"Contact '{name}' with phone '{phone}' has been added."


@input_error
def change_phone(name, phone):
    if name not in contacts:
        return f"!!! Contact '{name}' does not exist !!!"
    contacts[name] = phone
    return f"The phone number for contact '{name}' has been changed to '{phone}'."


@input_error
def get_phone(name):
    if name not in contacts:
        return f"Contact '{name}' does not exist."
    return f"The phone number for contact '{name}' is '{contacts[name]}'."


def show_all_contacts():
    if not contacts:
        return "The contact list is empty."
    result = "Contacts:\n"
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result


command_text = 'Hello, Add, Change, Phone, Show all, Good bye, Close or Exit'


def main():
    print(f"Enter command: {command_text}")
    while True:
        command = input("Enter command > ").lower()
        if command == "hello":
            print(f"How can I help you?")
        elif command == "add":
            try:
                name, phone = input("Enter Name & Phone > ").lower().split()
                print(add_contact(name, phone))
            except ValueError:
                print(
                    "Invalid input. Please, enter both Name & Phone separated by a space.")
        elif command == "change":
            try:
                name, phone = input(
                    "Name & Phone to change Phone > ").lower().split()
                print(change_phone(name, phone))
            except ValueError:
                print(
                    "Invalid input. Please, enter both Name & Phone separated by a space.")
        elif command == "phone":
            name = input("Enter Name to look Phone> ").lower()
            print(get_phone(name))
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
