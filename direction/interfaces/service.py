from abc import ABCMeta, abstractproperty, abstractmethod

__metaclass__ = type
__all__ = ['DirectService', 'DirectAPI', 'Configuration', 'Method', 'Router']

class DirectService:
    """
    A service linking an API to a router and providing a remote interface.
    """
    __metaclass__ = ABCMeta

    @abstractproperty
    def api(self):
        """
        Returns a JSON representation of the API presented by this service.
        """
    @abstractproperty
    def router(self):
        """
        Returns the router for this service.
        """

class DirectAPI:
    """
    Represents an API comprising multiple classes and methods.
    """
    __metaclass__ = ABCMeta

    @abstractproperty
    def type(self):
        """
        Type of API provided by this object.

        This currently always returns "remoting".
        """
    @abstractproperty
    def url(self):
        """
        URL at which the router for this API can be found.
        """
    @abstractproperty
    def actions(self):
        """
        List of L{Configuration} objects representing the available actions
        provided by the router for this API.
        """
    @abstractmethod
    def add_action(self, action):
        """
        Add an action to this API.
        """


class DirectAction:
    """
    Defines the API configuration interface.
    """
    __metaclass__ = ABCMeta

    @abstractproperty
    def name(self):
        """
        Class name to be called.
        """
    @abstractproperty
    def add_method(self, method):
        """
        Add a Method object.
        """


class Method:
    """
    Represents a method that can be remoted.
    """
    __metaclass__ = ABCMeta

    @abstractproperty
    def name(self):
        """
        Represents the method name to be called.
        """

    @abstractproperty
    def arguments(self):
        """
        Dictionary of keyword arguments.
        """


class Router:
    """
    Routes requests to the appropriate class and returns the results.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def callback(self, request):
        """
        Parses a request into individual calls to be made.
        """

    @abstractmethod
    def dispatch(self, klass, method, arguments):
        """
        Calls the target method with the specified arguments and returns the
        result.
        """
