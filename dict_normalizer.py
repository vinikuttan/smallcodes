#!/usr/bin/python

__author__ = 'vineesh'


def merge_nested_dict(mydict):
    """
    flattening nested dict
    """
    if isinstance(mydict, dict):
        result = mydict.copy()

        for each in mydict:
            if isinstance(mydict[each], dict):
                result[each] = mydict[each].keys()
                result.update(merge_nested_dict(mydict[each]))
            else:
                result[each] = mydict[each]
        return result

    else:
        return mydict


def merge_two_dicts(left, right):
    """
    replacing left dictionary with updated right dictionary
    """
    if isinstance(left, dict) and isinstance(right, dict):
        result = left.copy()
        for each in right:
            if each in left:
                result[each] = merge_two_dicts(left[each], right[each])
            else:
                result[each] = right[each]
        return result
    else:
        return right


if __name__=="__main__":
    input_dict = {'a':1, 'b':{'c':2, 'e': 4}, 'd': '3'}
    left_dict = {'a':1, 'b': 2, 'c':{'d':3, 'e':4}}
    right_dict = {'a':1, 'b': 2, 'c': 3}

    # merging nested python dictionaries
    print merge_nested_dict(input_dict)

    # deep merging two dictionaries
    print merge_two_dicts(left_dict, right_dict)
