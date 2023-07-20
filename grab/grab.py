"""
@file     grab.py
@brief    Utils for manipulating strings.
@date     20/07/2023
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
        start (str): The start of the substring.
        end (str): The end of the substring.

    Returns:
        str: The substring between the start and end strings.

    Raises:
        LookupError: If the start or end strings are not found.
    """
    len_start = len(start)
    start_index = text.find(start)
    end_index = text.find(end, start_index + len_start)

    if -1 in (start_index, end_index):
        raise LookupError

    return text[start_index + len_start:end_index]


def grab_all(text, *, start, end):
    """
    Yield all substrings from a string.

    Usage:
        grab_all("Http 200 OK Http 404 Not Found", start="Http ", end=" OK")
        >> ("200", "404")

    Args:
        text (str): The string to be searched.
        start (str): The start of the substring.
        end (str): The end of the substring.

    Yields:
        str: The next substring between the start and end strings.
    """
    len_start = len(start)
    len_end = len(end)

    while True:
        start_index = text.find(start)
        end_index = text.find(end, start_index + len_start)

        if -1 in (start_index, end_index):
            return

        yield text[start_index + len_start:end_index]
        text = text[end_index + len_end:]
