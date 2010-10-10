from abc import ABCMeta, abstractmethod, abstractproperty

__metaclass__ = type
__all__ = ['DirectClient', 'Stub']

class DirectClient:
    __metaclass__ = ABCMeta

    @abstractmethod
    def initialize(self, api):
        """
        Initialize the client with an API.
        """
    @abstractmethod
    def call(self):
        """
        Receive and handle a request.
        """

class Stub:
    __metaclass__ = ABCMeta

    @abstractmethod
    def initialize(self, configuration):
        """
        Initialize this stub with a Configuration.
        """

    @abstractmethod
    def call(self, transaction):
        """
        Receive and handle a transaction.
        """
