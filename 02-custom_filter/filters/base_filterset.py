from .base_filter import Filter

class FilterSetMetaclass(type):
    def __new__(cls, name, bases, attrs):
        new_class = super().__new__(cls, name, bases, attrs)
        new_class._filters = cls.get_filters(attrs)
        return new_class
    
    @classmethod
    def get_filters(cls, attrs):
        filters = []
        for k, v in attrs.items():
            if isinstance(v, Filter):
                v.set_key(k)
                filters.append((k, v))
        return filters

class BaseFilterSet(metaclass=FilterSetMetaclass):

    def __init__(self, request):
        self._data = {}
        self.get_data_from_request(request)
        
    def get_data_from_request(self, request):
        for k, f in self._filters:
            v = f.get(request)

            if v is None and not f.required:
                continue

            if not f.validator(v):
                raise ValueError(f"{k} is a class {f.__class__.__name__} got {v}")
            self._data[k] = v
    
    @property
    def data(self):
        return self._data