"""Handle some behavior here."""
from .contact import Contact, ContactSerializer
from .db_handler import DBHandler, CSVManager

manager = CSVManager('tests/sample.csv', serializer=ContactSerializer())
db_handler = DBHandler(manager=manager)
_contacts = db_handler.all()


def add(first_name, last_name, alias, email, phone):
    """Add a new entry to the contact list."""
    contact = Contact(first_name=first_name, last_name=last_name,
                      alias=alias, email=email, phone=phone)
    db_handler.save(contact)


def search(search_term):
    for contact in _contacts:
        if search_term in contact.search_helper():
            print(contact)
