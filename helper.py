#!/usr/bin/python


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
    

        
    
