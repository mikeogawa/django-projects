from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass     
class Filter(ABC):
    
    weight = 0
    key = None
    required = False
    
    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass
    
    def set_key(self, key):
        self.key = key
    
    @abstractmethod
    def get(self, request):
        """get request and extract"""
    
    @abstractmethod
    def validator(self, value):
        """set validator"""