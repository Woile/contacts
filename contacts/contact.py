
class ContactCSVSerializer:

    def read(self, line):
        return Contact(
            pk=line[0],
            first_name=line[1],
            last_name=line[2],
            alias=line[3],
            email=line[4],
            phone=line[5],
            in_db=True)

    def write(self, instance):
        return [
            instance.pk,
            instance.first_name,
            instance.last_name,
            instance.alias,
            instance.email,
            instance.phone
        ]


class Contact:
    """In memory representation of a contact."""

    def __init__(self, pk=None, first_name=None, last_name=None, alias=None,
                 email=None, phone=None, in_db=False):
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

    def __str__(self):
        """Print representation."""
        msg = '({0})\t{1} ({2}) {3}\t{4}\t{5}'
        return msg.format(self.pk, self.first_name, self.alias, self.last_name,
                          self.email, self.phone)

    def serialize(self):
        """Curate data to be stored in db."""
        msg = '{0},{1},{2},{3},{4},{5}'
        return msg.format(self.pk, self.first_name, self.last_name,
                          self.alias, self.email, self.phone)
