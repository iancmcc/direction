from json import dumps
from inspect import getargspec
from itertools import izip_longest, imap
from .interfaces import DirectAPI, DirectAction, Method, Serializable

_nocast = lambda x:x

class RemoteAPI(DirectAPI, Serializable):
    _type = 'remoting'
    _actions = None

    def __init__(self, url):
        self._actions = {}
        self._url = url

    @property
    def actions(self):
        return self._actions

    @property
    def url(self):
        return self._url

    @property
    def type(self):
        return self._type

    def add_action(self, action):
        assert isinstance(action, DirectAction)
        self._actions[action.name] = action

    def serialize(self):
        return {'type':self.type, 'url': self.url, 'actions':self.actions}


class ActionImpl(DirectAction, Serializable):
    _name = ''
    _methods = None

    def __init__(self, name):
        self._methods = {}
        self._name = name

    @property
    def name(self):
        return self._name

    def add_method(self, method):
        assert isinstance(method, Method)
        self._methods[method.name] = method

    def serialize(self):
        return self._methods


class MethodImpl(Method, Serializable):
    _name = ''
    _arguments = None
    _func = None

    def __init__(self, func):
        assert callable(func)
        self._func = func
        self._arguments = {}
        self._name = func.__name__
        spec = getargspec(func)
        self._arguments.update(
                izip_longest(reversed(spec.args),
                             imap(type, reversed(spec.defaults or ())),
                             fillvalue=_nocast))

    @property
    def name(self):
        return self._name

    @property
    def arguments(self):
        return self._arguments

    def serialize(self):
        return self._arguments.keys()
