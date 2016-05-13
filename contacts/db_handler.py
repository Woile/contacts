import csv
from contacts import ContactCSVSerializer


class CSVManager:

    def __init__(self, db_name, serializer=None):
        self.db_name = db_name
        if serializer is None:
            serializer = ContactCSVSerializer()
        self.serializer = serializer

    def __enter__(self):
        self.rfile = open(self.db_name)  # read
        self.afile = open(self.db_name, 'a')  # append
        return self

    def __exit__(self, type, value, traceback):
        self.rfile.close()
        self.afile.close()

    def all(self):
        reader = csv.reader(self.rfile)
        indexes = []
        qs = []
        for line in reader:
            indexes.append(line[0])
            qs.append(self.serializer.read(line))
        return qs, indexes

    def save_bulk(self, qs):
        pass

    def save(self, instance):
        if not isinstance(instance, list):
            instance = self.serializer.write(instance)
        writer = csv.writer(self.afile)
        writer.writerow(instance)


class DBHandler:
    """DB Abstraction."""

    def __init__(self, manager=None):
        if manager is None:
            manager = CSVManager('contacts.csv')
        self.manager = manager
        self.queryset = None
        self.pk_index = []

    def load_db_in_memory(self):
        with self.manager as manager:
            self.queryset, self.pk_index = manager.all()

    def save_collection(self):
        with self.manager as manager:
            manager.save_bulk(self.queryset)

    def save(self, instance, update=False):
        if not update and instance.pk in self.pk_index:
            return
        with self.manager as manager:
            manager.save(instance)
