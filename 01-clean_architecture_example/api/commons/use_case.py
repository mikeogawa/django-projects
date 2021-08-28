from abc import ABC, abstractmethod

class BaseUseCase(ABC):

    @abstractmethod
    def __init__(self):
        """
        define repository
        """

    @abstractmethod
    def execute(self, *args, **kwargs):
        """
        create a running function
        """