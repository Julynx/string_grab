"""
@file     grab.py
@brief    Utils for manipulating strings.
@date     21/07/2023
@author   Julio Cabria
"""


def grab(text, *, start, end):
    """
    Grab a substring from a string.

    Usage:
        grab("Http 200 OK", start="Http ", end=" OK")
        >> "200"

    Args:
        text (str): The string to be searched.
        start (str): The start string.
        end (str): The end string.

    Returns:
        str: The substring between the 'start' and 'end' strings.

    Raises:
        TypeError: If the 'text', 'start' or 'end' arguments are not strings.
        LookupError: If the 'start' or 'end' strings are not in 'text'.
    """
    _validate_args(func_name="grab", args_dict=locals(), expects=str)

    len_start = len(start)
    start_index = text.find(start)
    end_index = text.find(end, start_index + len_start)

    if -1 in (start_index, end_index):
        raise LookupError("Could not find 'start' or 'end' in 'text'.")

    return text[start_index + len_start:end_index]


def grab_all(text, *, start, end):
    """
    Yield all substrings from a string.

    Usage:
        grab_all("Http 200. Http 404.", start="Http ", end=".")
        >> ("200", "404")

    Args:
        text (str): The string to be searched.
        start (str): The start string.
        end (str): The end string.

    Yields:
        str: The next substring between the 'start' and 'end' strings.

    Raises:
        TypeError: If the 'text', 'start' or 'end' arguments are not strings.
    """
    _validate_args(func_name="grab_all", args_dict=locals(), expects=str)

    len_start = len(start)
    len_end = len(end)

    while True:
        start_index = text.find(start)
        end_index = text.find(end, start_index + len_start)

        if -1 in (start_index, end_index):
            return

        yield text[start_index + len_start:end_index]
        text = text[end_index + len_end:]


def _validate_args(*, func_name, args_dict, expects):
    """
    Raises a TypeError if any of the arguments is not of the expected type.

    Args:
        func_name (str): The name of the function.
        args_dict (dict): The arguments dictionary.
        expects (type): The expected type.

    Raises:
        TypeError: If any of the arguments is not of the expected type.
    """
    for arg_name, arg_value in args_dict.items():

        if isinstance(arg_value, expects):
            continue

        raise TypeError(f"{func_name}() expected str for '{arg_name}', "
                        f"got {type(arg_value).__name__} instead.")
