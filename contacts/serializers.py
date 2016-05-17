__all__ = ('CSVSerializer',)


class CSVSerializer:

    def __init__(self, klass, field_order):
        self._klass = klass
        self._field_order = field_order

    def serialize(self, instance):
        """Curate data to be stored in db."""
        return [getattr(instance, key) for key in self._field_order]

    def deserialize(self, line):
        """Convert data into instance."""
        return self._klass(raw=line, **dict(zip(self._field_order, line)))
