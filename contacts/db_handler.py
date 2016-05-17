import csv


class CSVManager:

    def __init__(self, db_name, serializer=None):
        self.db_name = db_name
        self.serializer = serializer
        self.indexes = []

    def __enter__(self):
        self.rfile = open(self.db_name)  # read
        self.afile = open(self.db_name, 'a')  # append
        return self

    def __exit__(self, type, value, traceback):
        self.rfile.close()
        self.afile.close()

    def all(self):
        """Parse csv and return instances."""
        qs = []
        indexes = []
        reader = csv.reader(self.rfile)
        for line in reader:
            indexes.append(int(line[0]))
            qs.append(self.serializer.csv.deserialize(line))

        self.indexes = indexes
        return qs

    def save_bulk(self, qs):
        pass

    def save(self, instance):
        """Save into csv."""
        if not self.indexes:
            self.all()  # Run to populate indexes.
        if instance.pk is None:
            instance.pk = max(self.indexes) + 1
            instance.in_db = True
        _line = self.serializer.csv.serialize(instance)
        writer = csv.writer(self.afile)
        writer.writerow(_line)
        return instance


class DBHandler:
    """DB Abstraction."""

    def __init__(self, manager=None):
        self._manager = manager
        self.queryset = []

    def all(self):
        with self._manager as manager:
            self.queryset = manager.all()
        return self.queryset

    def filter(self):
        """Filter based on provided information."""
        pass

    def save_bulk(self):
        """Save multiple instances at once."""
        with self._manager as manager:
            manager.save_bulk(self.queryset)

    def save(self, instance, update=False):
        """Save a single instance."""
        with self._manager as manager:
            self.queryset.append(manager.save(instance))
