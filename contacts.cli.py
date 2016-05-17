import contacts

def add():
    first_name = input('First name: ')
    last_name = input('Last name: ')
    alias = input('Nickname: ')
    email = input('Email: ')
    phone = input('Phone: ')
    contacts.add(first_name, last_name, alias, email, phone)


def search():
    search_term = input('Search: ')
    contacts.search(search_term)


def list_contacts():
    """Show all the contacts available."""
    for contact in contacts._contacts:
        print(contact)
