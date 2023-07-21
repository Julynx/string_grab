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

    try:
        parts = text.split(start, 1)[1].split(end, 1)
        _ = parts[1]  # Raises IndexError if 'end' not in 'text'.
        return parts[0]

    except IndexError as index_error:
        raise LookupError("Could not find 'start' or 'end' in 'text'.") \
            from index_error


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

    while True:

        try:
            text = text.split(start, 1)[1]
            parts = text.split(end, 1)
            _ = parts[1]  # Raises IndexError if 'end' not in 'text'.
            yield parts[0]

        except IndexError:
            return


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

        raise TypeError(f"{func_name}() expected {expects.__name__} for "
                        f"'{arg_name}', got {type(arg_value).__name__}.")
