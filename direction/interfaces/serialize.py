from abc import ABCMeta, abstractmethod

__metaclass__ = type
__all__ = ['Serializable']

class Serializable:
    """
    An object that can be serialized.
    """
    @abstractmethod
    def serialize(self):
        """
        Return a serialized version of this object.
        """
