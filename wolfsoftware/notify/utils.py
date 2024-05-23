"""
This module provides utilities for working with color-coded messages in the terminal.

It uses ANSI color codes and the colorama library for cross-platform support.

The primary function in this module is:
- `get_color_codes`: Returns a dictionary with ANSI color codes based on the specified color parameter.

Returns:
--------
The module returns formatted color codes for use in terminal messages, ensuring that the text appears
with the specified color and style (e.g., bold).

Raises:
-------
- NotifyValueError: Raised if an invalid color format is provided. Valid formats include 'color', 'color+bold', or 'bold'.
- NotifyValueError: Raised if an invalid color component is specified. Allowed values are predefined color constants.

Example Usage:
--------------
To use the color code utility function, you can import it and get the required color codes as follows:

    from your_module_name import get_color_codes

    color_codes = get_color_codes('red+bold')
    print(f"{color_codes['color']}This is a bold red message{color_codes['reset']}")

"""
# pylint: disable=relative-beyond-top-level

import re
import colorama

from .exceptions import NotifyValueError


def get_color_codes(color: str = '') -> dict:
    """
    Generate ANSI color codes for terminal message formatting.

    This function returns a dictionary containing ANSI color codes based on the specified color
    parameter. It supports various colors and styles, including bold text. The colorama library
    is used to ensure compatibility across different platforms.

    Arguments:
    ----------
    color (str, optional): The color and style to apply. It can be a color, 'color+bold', or 'bold'.
                           Default is '' (no color).

    Returns:
    --------
    dict: A dictionary with keys 'color' and 'reset', containing the respective ANSI codes.
          - 'color': The ANSI code(s) for the specified color and style.
          - 'reset': The ANSI code to reset the text formatting.

    Raises:
    -------
    NotifyValueError: If an invalid color component is specified. Allowed values are:
                      black, blue, cyan, green, grey, magenta, red, white, yellow, bold, reset.
    NotifyValueError: If an invalid color format is provided. Valid formats include 'color', 'color+bold', or 'bold'.

    Example Usage:
    --------------
    To use the color code utility function, you can get the required color codes as follows:

        color_codes = get_color_codes('red+bold')
        print(f"{color_codes['color']}This is a bold red message{color_codes['reset']}")
    """
    colors: dict[str, str] = {
        'black': colorama.Fore.BLACK,
        'blue': colorama.Fore.BLUE,
        'cyan': colorama.Fore.CYAN,
        'green': colorama.Fore.GREEN,
        'grey': colorama.Fore.LIGHTBLACK_EX,
        'magenta': colorama.Fore.MAGENTA,
        'red': colorama.Fore.RED,
        'white': colorama.Fore.WHITE,
        'yellow': colorama.Fore.YELLOW,
        'bold': colorama.Style.BRIGHT,
        'reset': colorama.Style.RESET_ALL
    }

    # Set color and style if specified
    color_code: str = ''
    if color:
        sanitized_color: str = re.sub(r'[^a-zA-Z+]', '', color).lower()  # Remove everything except alphabetic characters and '+', and convert to lowercase
        parts: list[str] = sanitized_color.split('+')
        if len(parts) > 2 or (len(parts) == 2 and 'bold' not in parts):
            raise NotifyValueError("Invalid color format. Use 'color', 'color+bold', or 'bold'.")

        color_code = ''
        for part in parts:
            if part in colors:
                color_code += colors[part]
            else:
                raise NotifyValueError(f"Invalid color component '{part}'. Allowed values are: {', '.join(colors.keys())}")

    reset_code: str = colors['reset'] if color_code else ''

    return {
        "color": color_code,
        "reset": reset_code
    }
