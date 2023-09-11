"""
@file     grab.py
@brief    Utils for manipulating strings.
@date     11/09/2023
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

    except (IndexError, ValueError) as error:
        raise LookupError("Could not find 'start' or 'end' in 'text'.") \
            from error


def grab_until(text, *, end):
    """
    Grab a substring from a string until the 'end' string is found.

    Usage:
        grab_until("Http 200 OK", end=" ")
        >> "Http"

    Args:
        text (str): The string to be searched.
        end (str): The end string.

    Returns:
        str: The substring until the 'end' string is found.

    Raises:
        TypeError: If the 'text' or 'end' arguments are not strings.
        LookupError: If the 'end' string is not in 'text'.
    """
    _validate_args(func_name="grab_until", args_dict=locals(), expects=str)

    try:
        parts = text.split(end, 1)
        _ = parts[1]  # Raises IndexError if 'end' not in 'text'.
        return parts[0]

    except (IndexError, ValueError) as error:
        raise LookupError("Could not find 'end' in 'text'.") from error


def grab_after(text, *, start):
    """
    Grab a substring from a string after the 'start' string is found.

    Usage:
        grab_after("Http 200 OK", start=" ")
        >> "200 OK"

    Args:
        text (str): The string to be searched.
        start (str): The start string.

    Returns:
        str: The substring after the 'start' string is found.

    Raises:
        TypeError: If the 'text' or 'start' arguments are not strings.
        LookupError: If the 'start' string is not in 'text'.
    """
    _validate_args(func_name="grab_after", args_dict=locals(), expects=str)

    try:
        return text.split(start, 1)[1]

    except (IndexError, ValueError) as error:
        raise LookupError("Could not find 'start' in 'text'.") from error


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

        except (IndexError, ValueError):
            return


def inject(text, insert, *, start, end):
    """
    Inject 'insert' in 'text' between two 'start' and 'end' strings.

    Args:
        text (str): The base string.
        insert (str): The string to be injected.
        start (str): The string before the injection point.
        end (str): The string after the injection point.

    Returns:
        str: The 'text' string with the 'insert' string injected.

    Raises:
        TypeError: If any of the arguments is not a string.
        LookupError: If the 'start' or 'end' strings are not in 'text'.
    """
    _validate_args(func_name="inject", args_dict=locals(), expects=str)

    try:
        prev_parts = text.split(start, 1)
        next_parts = prev_parts[1].split(end, 1)
        return "".join((prev_parts[0], start, insert, end, next_parts[1]))

    except (IndexError, ValueError) as error:
        raise LookupError("Could not find 'start' or 'end' in 'text'.") \
            from error


def inject_until(text, insert, *, end):
    """
    Inject 'insert' in 'text', replacing everything before the 'end' string.

    Args:
        text (str): The base string.
        insert (str): The string to be injected.
        end (str): The string after the injection point.

    Returns:
        str: The 'text' string with the 'insert' string injected.

    Raises:
        TypeError: If any of the arguments is not a string.
        LookupError: If the 'end' string is not in 'text'.
    """
    _validate_args(func_name="inject_until", args_dict=locals(), expects=str)

    try:
        parts = text.split(end, 1)
        return "".join((insert, end, parts[1]))

    except (IndexError, ValueError) as error:
        raise LookupError("Could not find 'end' in 'text'.") from error


def inject_after(text, insert, *, start):
    """
    Inject 'insert' in 'text', replacing everything after the 'start' string.

    Args:
        text (str): The base string.
        insert (str): The string to be injected.
        start (str): The string before the injection point.

    Returns:
        str: The 'text' string with the 'insert' string injected.

    Raises:
        TypeError: If any of the arguments is not a string.
        LookupError: If the 'start' string is not in 'text'.
    """
    _validate_args(func_name="inject_after", args_dict=locals(), expects=str)

    try:
        parts = text.split(start, 1)
        _ = parts[1]  # Raises IndexError if 'start' not in 'text'.
        return "".join((parts[0], start, insert))

    except (IndexError, ValueError) as error:
        raise LookupError("Could not find 'start' in 'text'.") from error


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
