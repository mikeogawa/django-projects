from .base_filter import Filter

class StringFilter(Filter):
    
    def __init__(self):
        pass

    def get(self, request):
        return request.GET.get(self.key)
    
    def validator(self, value):
        return isinstance(value, str)