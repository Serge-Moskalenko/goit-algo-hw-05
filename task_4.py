def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."

    return inner

def change_number_input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter the argument for the command"
        

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    print("Available commands:\nheloo\nadd\nall\nchange\nphone\nclose or exit")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "all":
            print(contacts)
        elif command == "change":
            print(change_number(args, contacts))
        elif command == "phone":
            print(print_phone(args, contacts))
        else:
            print("Invalid command.")

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args

    if name in contacts:
        user=input("Do you want re-record contact? (yes/no):").strip().lower()

        if user == "yes":
            contacts[name] = phone
            return "contact update"
        elif user == "no":
            return "contact not added"
        else:
            return "Invalid command."
    else: 
        contacts[name] = phone
        return "Contact added."
    
@change_number_input_error   
def change_number(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "number is change"
    else:
        return f"{name} is not found"

def print_phone(args, contacts):
    name,*ar = args
    if name in contacts:
        return contacts[name]
    else:
        return f"{name} is not found"


if __name__ == "__main__":
    try:
        main()
    except ValueError as error:
        print(f"error:{error}")