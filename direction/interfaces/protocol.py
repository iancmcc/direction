from abc import ABCMeta, abstractmethod, abstractproperty

__metaclass__ = type
__all__ = ['Transaction', 'Request', 'SuccessResult', 'FailureResult',
           'Response']

class Transaction:
    """
    A transaction representing a single remote method call.
    """
    __metaclass__ = ABCMeta

    @abstractproperty
    def action(self):
        """
        Action.
        """
    @abstractproperty
    def method(self):
        """
        Method.
        """
    @abstractproperty
    def data(self):
        """
        Data.
        """
    @abstractproperty
    def type(self):
        """
        Type.
        """
    @abstractproperty
    def tid(self):
        """
        Transaction ID.
        """


class Request:
    """
    A set of transactions representing a single request to the service.
    """
    __metaclass__ = ABCMeta

    @abstractproperty
    def transactions(self):
        """
        The set of Transactions that came with this request.
        """


class Result:
    """
    The result of a single transaction call.
    """
    __metaclass__ = ABCMeta

    def type(self):
        """
        Type of this result.
        """


class SuccessResult(Result):
    """
    A successful result.
    """
    @abstractproperty
    def action(self):
        """
        Action that produced this result.
        """
    @abstractproperty
    def method(self):
        """
        Method that produced this result.
        """
    @abstractproperty
    def result(self):
        """
        Result of the method call.
        """
    @abstractproperty
    def tid(self):
        """
        Transaction ID for this result.
        """


class FailureResult(Result):
    """
    A failed result.
    """
    @abstractproperty
    def message(self):
        """
        Message indicating what went wrong.
        """
    @abstractproperty
    def where(self):
        """
        Information about where the error occurred.
        """


class Response:
    """
    A response containing multiple serialized TransactionResults.
    """
    __metaclass__ = ABCMeta

    @abstractproperty
    def results(self):
        """
        All the results for this response.
        """
