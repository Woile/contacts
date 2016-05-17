from .serializers import CSVSerializer


class ContactSerializer:

    def __init__(self):
        field_order = ('pk', 'first_name', 'last_name', 'alias',
                       'email', 'phone', 'in_db')
        self.csv = CSVSerializer(Contact, field_order)


class Contact:
    """In memory representation of a contact."""

    def __init__(self, pk=None, first_name=None, last_name=None, alias=None,
                 email=None, phone=None, in_db=False, raw=None):
        """Initialization of a single contact.

        :param pk:
        :type pk: int
        :param first_name:
        :type first_name: unicode
        :param last_name:
        :type last_name: unicode
        :param alias:
        :type alias: unicode
        :param email:
        :type email: unicode
        :param phone:
        :type phone: unicode
        :param in_db: if there is a copy in the database set True
        :type in_db: bool
        """
        self.pk = pk
        self.first_name = first_name
        self.last_name = last_name
        self.alias = alias
        self.email = email
        self.phone = phone
        self.in_db = in_db
        self.raw = raw

    def __str__(self):
        """Print representation."""
        alias = '({0}) '.format(self.alias) if self.alias else ''

        msg = '({0})\t{1} {2}{3:20}\t{4:20}\t\t{5}'
        return msg.format(self.pk, self.first_name, alias, self.last_name,
                          self.email, self.phone)

    def search_helper(self):
        _helper = '{0}{1}{2}{3}{4}{5}'
        return _helper.format(self.pk, self.first_name, self.alias, self.last_name,
                              self.email, self.phone).lower()
