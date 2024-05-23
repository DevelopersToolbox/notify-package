"""
This module provides a custom exception class for handling notification-related value errors.

The primary purpose of this module is to define a specific exception that can be raised when
invalid values are encountered during the execution of notification functions, such as when
specifying incorrect color components for terminal message formatting.

Classes:
--------
- `NotifyValueError`: A custom exception class for notification-related value errors.

Class Details:
--------------
- `NotifyValueError`: Inherits from the base Exception class. It is used to signal errors
  related to invalid values in the notification system.

Example Usage:
--------------
To use the custom exception class, you can import and raise it as follows:

    from your_module_name import NotifyValueError

    if invalid_color_component:
        raise NotifyValueError("Invalid color component specified.")

"""


class NotifyValueError(Exception):
    """
    Custom exception class for notification-related value errors.

    This exception is raised when an invalid value is encountered within the notification system,
    such as when specifying an invalid color component for terminal message formatting.

    Arguments:
    ----------
    Exception (type): Inherits from the base Exception class to provide custom error handling.

    Example Usage:
    --------------
    To raise this exception, you can use it as follows:

        if invalid_color_component:
            raise NotifyValueError("Invalid color component specified.")
    """
