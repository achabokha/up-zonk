##
## from here, just the one needed no packages, required
## https://github.com/okunishinishi/python-stringcase/blob/50fe41d3c9bebf001f24fc49b89fe023b5eba12c/stringcase.py#L25
##

import re
import inflect

inflect_engine = inflect.engine()

def lowercase(string):
    """Convert string into lower case.
    Args:
        string: String to convert.
    Returns:
        string: Lowercase case string.
    """

    return str(string).lower()


def uppercase(string):
    """Convert string into upper case.
    Args:
        string: String to convert.
    Returns:
        string: Uppercase case string.
    """

    return str(string).upper()


def capitalcase(string):
    """Convert string into capital case.
    First letters will be uppercase.
    Args:
        string: String to convert.
    Returns:
        string: Capital case string.
    """

    string = str(string)
    if not string:
        return string
    return uppercase(string[0]) + string[1:]


def camelcase(string):
    """ Convert string into camel case.
    Args:
        string: String to convert.
    Returns:
        string: Camel case string.
    """

    string = re.sub(r"^[\-_\.]", '', str(string))
    if not string:
        return string
    return lowercase(string[0]) + re.sub(r"[\-_\.\s]([a-z])", lambda matched: uppercase(matched.group(1)), string[1:])


def pascalcase(string):
    """Convert string into pascal case.
    Args:
        string: String to convert.
    Returns:
        string: Pascal case string.
    """

    return capitalcase(camelcase(string))

def spacecase(string):
    return string.replace('-', ' ').replace('_', ' ')

def underscorecase(string):
    return string.replace('-', '_')

def nospacescase(string):
    return string.replace(' ', '')


def plural(string):
    return inflect_engine.plural(string)


def quickTest():

    print('SnakeToPascal: ', pascalcase('snake_to_pascal'))
    print('snakeToCamel: ', camelcase('snake_to_camel'))

    print("KebabToCamel: ", camelcase("kebab-to-camel"))
    print("KebabToPascal: ", pascalcase("kebab-to-pascal"))

# quickTest()