import click
import contacts
import cfg

contacts.configure(DB_PATH=cfg.DB_PATH)
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
__version__ = '0.1.0'


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version=__version__)
def contact():
    """Simple command line contacts manager which uses CSV as storage."""
    pass


@contact.command()
@click.argument('first_name')
@click.argument('last_name')
@click.argument('alias')
@click.argument('email')
@click.argument('phone')
def add(**kwargs):
    """Add new entry to the contact list."""
    first_name = kwargs.get('first_name')
    last_name = kwargs.get('last_name')
    alias = kwargs.get('alias')
    email = kwargs.get('email')
    phone = kwargs.get('phone')
    contacts.add(first_name, last_name, alias, email, phone)


@contact.command()
@click.argument('search_term')
def search(**kwargs):
    """Search contacts."""
    search_term = kwargs.get('search_term')
    contacts.search(search_term)


@contact.command()
def show():
    """Show all the contacts stored."""
    for contact in contacts._contacts:
        print(contact)


if __name__ == '__main__':
    contact()