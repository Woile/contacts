"""Handle some behavior here."""
import click

from .contact import Contact, ContactSerializer
from .db_handler import DBHandler, CSVManager


manager = CSVManager('contacts.csv', serializer=ContactSerializer())
db_handler = DBHandler(manager=manager)
_contacts = db_handler.all()


def add(first_name, last_name, alias, email, phone):
    """Add a new entry to the contact list."""
    contact = Contact(first_name=first_name, last_name=last_name,
                      alias=alias, email=email, phone=phone)
    db_handler.save(contact)
    click.echo('Done.')


def search(search_term):
    """Search given term."""
    search_term = search_term.lower()
    matches = 0
    for contact in _contacts:
        if search_term in contact.search_helper():
            click.echo(contact)
            matches += 1

    if not matches:
        click.echo('No matches found.')


def configure(**kwargs):
    db_path = kwargs.get('DB_PATH')
    if db_path is not None:
        global manager
        global db_handler
        global _contacts

        manager = CSVManager(db_path, serializer=ContactSerializer())
        db_handler = DBHandler(manager=manager)
        _contacts = db_handler.all()
