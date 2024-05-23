"""
This module provides a collection of notification functions.

It also provides custom exceptions for handling various types of messages within the Wolf Software Notify package.

The main functionalities offered by this module include:
- Displaying success, warning, error, failure, informational, and system messages.
- Handling custom exceptions related to notification values.
- Retrieving the package version using importlib.metadata.

Modules and Functions:
----------------------
- `success_message`: Displays a success message.
- `warning_message`: Displays a warning message.
- `error_message`: Displays an error message.
- `failure_message`: Displays a failure message.
- `info_message`: Displays an informational message.
- `system_message`: Displays a system message.

Exceptions:
-----------
- `NotifyValueError`: Custom exception for handling notification-related value errors.

Attributes:
-----------
- `__version__`: str
    The version of the wolfsoftware.notify package. If the package version cannot be retrieved, it is set to 'unknown'.
- `__all__`: list[str]
    A list of public objects of this module, as interpreted by import *.

Example Usage:
--------------
To use the notification functions, you can import them as follows:

    from notify import success_message, warning_message

    success_message("Operation completed successfully.")
    warning_message("This is a warning message.")

To handle exceptions, you can use NotifyValueError:

    try:
        # Some operation that may raise NotifyValueError
    except NotifyValueError as e:
        print(f"An error occurred: {e}")

"""

import importlib.metadata

from .notify import success_message, warning_message, error_message, failure_message, info_message, system_message
from .exceptions import NotifyValueError
from .utils import get_color_codes

try:
    __version__: str = importlib.metadata.version('wolfsoftware.notify')
except importlib.metadata.PackageNotFoundError:
    __version__ = 'unknown'

__all__: list[str] = [
    'success_message',
    'warning_message',
    'error_message',
    'failure_message',
    'info_message',
    'system_message',
    'get_color_codes',
    'NotifyValueError'
]
