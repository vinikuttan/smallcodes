#!/usr/bin/python
""" 
Generic Utility functionalities
"""


def deep_getattr(obj, attr, default=None):
    """
    @example:
        deep_getattr(organisation, 'department.employee.id', default=0)
        
    """
    attributes= attr.split('.')
    for each in attributes:
        try:
            obj = getattr(obj, each)
        except AttributeError:
            return default
    return obj


class FrozenDict(dict):
    def __hash__(self):
        return hash(tuple(sorted(self.items())))

    def _immutable(self, *args, **kws):
        raise TypeError('object is immutable')

    __setitem__ = _immutable
    __delitem__ = _immutable
    clear = _immutable
    update = _immutable
    setdefault = _immutable
    pop = _immutable
    popitem = _immutable


def freeze(obj):
    if isinstance(obj, dict):
        return FrozenDict((k, freeze(v)) for k, v in obj.items())
    elif isinstance(obj, list):
        return tuple(freeze(el) for el in obj)
    elif isinstance(obj, set):
        return frozenset(obj)
    else:
        return obj   
