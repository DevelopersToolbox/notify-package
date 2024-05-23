"""
This module defines functions for printing formatted messages to the terminal.

The main purpose of this module is to provide utility functions for displaying
success, warning, error, information, and system messages with specific color
and style formatting using predefined constants.

Functions:
----------
- `success_message`: Prints a success message formatted with bold and green text.
- `warning_message`: Prints a warning message formatted with bold and yellow text.
- `error_message`: Prints an error message formatted with bold and red text.
- `failure_message`: Alias for `error_message`, prints an error message formatted with bold and red text.
- `info_message`: Prints an informational message formatted with bold and cyan text.
- `system_message`: Prints a system message formatted with bold and grey text.

Example Usage:
--------------
To use the notification functions, you can import them as follows:

    from notify import success_message, warning_message, error_message, info_message, system_message

    print(success_message("Operation completed successfully."))
    print(warning_message("This is a warning message."))
    print(error_message("An error occurred."))
    print(info_message("This is some information."))
    print(system_message("System update available."))
"""
# pylint: disable=relative-beyond-top-level, too-many-arguments

from functools import partial

from .utils import get_color_codes
from .exceptions import NotifyValueError


def format_message(
    message: str,
    prompt: str,
    color: str,
    scope: str,
    prompt_prefix: str,
    prompt_suffix: str
) -> str:
    """
    Format a message with a specific color and scope.

    Arguments:
        message (str): The message to be printed.
        prompt (str): The prompt to be displayed inside brackets.
        color (str): The color to apply.
        scope (str): The scope of the color ('whole message', 'whole prompt', 'inside brackets').
        prompt_prefix (str): The prefix to add before the prompt.
        prompt_suffix (str): The suffix to add after the prompt.

    Returns:
        str: The formatted message.

    Raises:
        NotifyValueError: If an invalid color or scope is provided.
    """
    try:
        codes: dict = get_color_codes(color)
    except NotifyValueError as err:
        raise NotifyValueError(f"Invalid color: {err}") from err

    if scope not in ['all', 'prompt', 'prompt_text']:
        raise NotifyValueError("Invalid scope. Use 'all', 'prompt', or 'prompt_text'.")

    if scope == 'all':
        return f"{codes['color']}{prompt_prefix}{prompt}{prompt_suffix} {message}{codes['reset']}"
    if scope == 'prompt':
        return f"{codes['color']}{prompt_prefix}{prompt}{prompt_suffix}{codes['reset']} {message}"
    if scope == 'prompt_text':
        return f"{prompt_prefix}{codes['color']}{prompt}{codes['reset']}{prompt_suffix} {message}"

    raise NotifyValueError(f"Unhandled scope: {scope}")


def success_message(
    message: str,
    color: str = 'green+bold',
    prompt: str = 'Success',
    scope: str = 'prompt_text',
    prompt_prefix: str = '[ ',
    prompt_suffix: str = ' ]'
) -> str:
    """
    Print a success message with a specific format.

    This function outputs a message indicating success, formatted with the specified color and style.

    Arguments:
        message (str): The success message to be printed.
        color (str, optional): The color to apply. Default is 'green'.
        prompt (str, optional): The prompt to use. Default is 'Success'.
        scope (str, optional): The scope of the color. Default is 'whole message'.
        prompt_prefix (str, optional): The prefix to add before the prompt. Default is '[ '.
        prompt_suffix (str, optional): The suffix to add after the prompt. Default is ' ]'.

    Returns:
        str: The formatted success message.

    Raises:
        NotifyValueError: If an invalid color or scope is provided.
    """
    return format_message(message, prompt, color, scope, prompt_prefix, prompt_suffix)


def warning_message(
    message: str,
    color: str = 'yellow+bold',
    prompt: str = 'Warning',
    scope: str = 'prompt_text',
    prompt_prefix: str = '[ ',
    prompt_suffix: str = ' ]'
) -> str:
    """
    Print a warning message with a specific format.

    This function outputs a message indicating a warning, formatted with the specified color and style.

    Arguments:
        message (str): The warning message to be printed.
        color (str, optional): The color to apply. Default is 'yellow'.
        prompt (str, optional): The prompt to use. Default is 'Warning'.
        scope (str, optional): The scope of the color. Default is 'whole message'.
        prompt_prefix (str, optional): The prefix to add before the prompt. Default is '[ '.
        prompt_suffix (str, optional): The suffix to add after the prompt. Default is ' ]'.

    Returns:
        str: The formatted warning message.

    Raises:
        NotifyValueError: If an invalid color or scope is provided.
    """
    return format_message(message, prompt, color, scope, prompt_prefix, prompt_suffix)


def error_message(
    message: str,
    color: str = 'red+bold',
    prompt: str = 'Error',
    scope: str = 'prompt_text',
    prompt_prefix: str = '[ ',
    prompt_suffix: str = ' ]'
) -> str:
    """
    Print an error message with a specific format.

    This function outputs a message indicating an error, formatted with the specified color and style.

    Arguments:
        message (str): The error message to be printed.
        color (str, optional): The color to apply. Default is 'red'.
        prompt (str, optional): The prompt to use. Default is 'Error'.
        scope (str, optional): The scope of the color. Default is 'whole message'.
        prompt_prefix (str, optional): The prefix to add before the prompt. Default is '[ '.
        prompt_suffix (str, optional): The suffix to add after the prompt. Default is ' ]'.

    Returns:
        str: The formatted error message.

    Raises:
        NotifyValueError: If an invalid color or scope is provided.
    """
    return format_message(message, prompt, color, scope, prompt_prefix, prompt_suffix)


# Creating an alias for the function
failure_message = partial(error_message, prompt='Failure')


def info_message(
    message: str,
    color: str = 'cyan+bold',
    prompt: str = 'Info',
    scope: str = 'prompt_text',
    prompt_prefix: str = '[ ',
    prompt_suffix: str = ' ]'
) -> str:
    """
    Print an informational message with a specific format.

    This function outputs a message indicating information, formatted with the specified color and style.

    Arguments:
        message (str): The informational message to be printed.
        color (str, optional): The color to apply. Default is 'cyan'.
        prompt (str, optional): The prompt to use. Default is 'Info'.
        scope (str, optional): The scope of the color. Default is 'whole message'.
        prompt_prefix (str, optional): The prefix to add before the prompt. Default is '[ '.
        prompt_suffix (str, optional): The suffix to add after the prompt. Default is ' ]'.

    Returns:
        str: The formatted informational message.

    Raises:
        NotifyValueError: If an invalid color or scope is provided.
    """
    return format_message(message, prompt, color, scope, prompt_prefix, prompt_suffix)


def system_message(
    message: str,
    color: str = 'grey+bold',
    prompt: str = 'System',
    scope: str = 'prompt_text',
    prompt_prefix: str = '[ ',
    prompt_suffix: str = ' ]'
) -> str:
    """
    Print a system message with a specific format.

    This function outputs a message indicating a system message, formatted with the specified color and style.

    Arguments:
        message (str): The system message to be printed.
        color (str, optional): The color to apply. Default is 'grey'.
        prompt (str, optional): The prompt to use. Default is 'System'.
        scope (str, optional): The scope of the color. Default is 'whole message'.
        prompt_prefix (str, optional): The prefix to add before the prompt. Default is '[ '.
        prompt_suffix (str, optional): The suffix to add after the prompt. Default is ' ]'.

    Returns:
        str: The formatted system message.

    Raises:
        NotifyValueError: If an invalid color or scope is provided.
    """
    return format_message(message, prompt, color, scope, prompt_prefix, prompt_suffix)
