from abc import ABCMeta, abstractmethod, abstractproperty

__metaclass__ = type
__all__ = ['Transaction', 'Request', 'TransactionResult', 'Response']

class Transaction:
    """
    A transaction representing a single remote method call.
    """
    __metaclass__ = ABCMeta
    _action = ''
    _method = ''
    _data = None
    _type = ''
    _tid = 0

    def __init__(self):
        self._data = {}

    @abstractproperty
    def action(self):
        return self._action

    @abstractproperty
    def method(self):
        return self._method

    @abstractproperty
    def data(self):
        return self._data

    @abstractproperty
    def type(self):
        return self._type

    @abstractproperty
    def tid(self):
        return self._tid


class Request:
    """
    A set of transactions representing a single request to the service.
    """
    __metaclass__ = ABCMeta
    _transactions = None
    def __init__(self):
        self._transactions = []

    @abstractproperty
    def transactions(self):
        return self._transactions


class TransactionResult:
    """
    The result of a single transaction call.
    """
    __metaclass__ = ABCMeta
    _type = ''
    _action = ''
    _method = ''
    _result = None
    _tid = 0

    @abstractproperty
    def type(self):
        return self._type

    @abstractproperty
    def action(self):
        return self._action

    @abstractproperty
    def method(self):
        return self._method

    @abstractproperty
    def result(self):
        return self._result

    @abstractproperty
    def tid(self):
        return self._tid


class Response:
    """
    A response containing multiple serialized TransactionResults.
    """
    __metaclass__ = ABCMeta
    _results = None

    def __init__(self):
        self._resultset= []

    @abstractproperty
    def resultset(self):
        return self._resultset
