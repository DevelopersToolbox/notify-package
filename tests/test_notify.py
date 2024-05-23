"""
This module contains unit tests for the Wolf Software Notify package, specifically testing the
functionality and output of message formatting functions, version definition, and custom prompt handling.

The tests ensure that:
- The package version is correctly defined and not set to 'unknown'.
- Each message function (success, warning, error, failure, info, and system) returns a string
  with the correct prefix indicating the message type.
- Custom colors, prompt prefixes, and suffixes are correctly applied to the formatted messages.
- Exceptions are raised appropriately for invalid color and scope inputs.

Functions:
----------
- `test_version`: Verifies that a version is defined for the package.
- `test_success_message_default_color`: Tests the default color of success messages.
- `test_success_message_custom_color_whole_message`: Tests custom color applied to the whole success message.
- `test_success_message_custom_color_whole_prompt`: Tests custom color applied to the whole success prompt.
- `test_success_message_custom_color_inside_brackets`: Tests custom color applied inside the success brackets.
- `test_custom_prompt_success_message`: Tests custom prompt in success messages.
- `test_success_message_invalid_color`: Tests success message with an invalid color.
- `test_warning_message_default_color`: Tests the default color of warning messages.
- `test_warning_message_custom_color`: Tests custom color applied to the whole warning message.
- `test_warning_message_custom_color_whole_prompt`: Tests custom color applied to the whole warning prompt.
- `test_warning_message_custom_color_inside_brackets`: Tests custom color applied inside the warning brackets.
- `test_custom_prompt_warning_message`: Tests custom prompt in warning messages.
- `test_warning_message_invalid_color`: Tests warning message with an invalid color.
- `test_error_message_default_color`: Tests the default color of error messages.
- `test_error_message_custom_color`: Tests custom color applied to the whole error message.
- `test_error_message_custom_color_whole_prompt`: Tests custom color applied to the whole error prompt.
- `test_error_message_custom_color_inside_brackets`: Tests custom color applied inside the error brackets.
- `test_custom_prompt_error_message`: Tests custom prompt in error messages.
- `test_error_message_invalid_color`: Tests error message with an invalid color.
- `test_failure_message`: Tests the alias function for error messages.
- `test_info_message_default_color`: Tests the default color of info messages.
- `test_info_message_custom_color`: Tests custom color applied to the whole info message.
- `test_info_message_custom_color_whole_prompt`: Tests custom color applied to the whole info prompt.
- `test_info_message_custom_color_inside_brackets`: Tests custom color applied inside the info brackets.
- `test_custom_prompt_info_message`: Tests custom prompt in info messages.
- `test_info_message_invalid_color`: Tests info message with an invalid color.
- `test_system_message_default_color`: Tests the default color of system messages.
- `test_system_message_custom_color`: Tests custom color applied to the whole system message.
- `test_system_message_custom_color_whole_prompt`: Tests custom color applied to the whole system prompt.
- `test_system_message_custom_color_inside_brackets`: Tests custom color applied inside the system brackets.
- `test_custom_prompt_system_message`: Tests custom prompt in system messages.
- `test_system_message_invalid_color`: Tests system message with an invalid color.
- `test_custom_prompt_prefix_suffix`: Tests message functions with custom prompt prefix and suffix.
- `test_get_color_codes_valid`: Tests get_color_codes with valid color format.
- `test_get_color_codes_invalid_format`: Tests get_color_codes with an invalid format.
- `test_get_color_codes_invalid_component`: Tests get_color_codes with an invalid color component.

Example Usage:
--------------
To run these tests, you can use a testing framework such as pytest:

    pytest test_notify.py

Each test function asserts that the respective message functions return strings that start with the
appropriate prefix, ensuring that the message formatting is correct, and handle errors appropriately.
"""
# pylint: disable=too-many-arguments, too-many-locals, too-few-public-methods

import re

import importlib.metadata

from typing import Optional

import pytest


from wolfsoftware.notify import (  # pylint: disable=import-error, no-name-in-module
    success_message,
    warning_message,
    error_message,
    failure_message,
    info_message,
    system_message,
    NotifyValueError,
    get_color_codes
)


class TestVersion:
    """
    Grouped tests for versions.
    """
    def test_version(self) -> None:
        """
        Test that a version is defined.

        This test verifies that the version of the package is defined and not set to 'unknown'.

        Asserts:
            The version is not None and not 'unknown'.
        """
        version: Optional[str] = None

        try:
            version = importlib.metadata.version('wolfsoftware.notify')
        except importlib.metadata.PackageNotFoundError:
            version = None

        assert version is not None, "Version should be set"  # nosec: B101
        assert version != 'unknown', f"Expected version, but got {version}"  # nosec: B101


class TestSuccessMessages:
    """
    Grouped tests for success_message function.
    """

    def test_success_message_default_color(self, test_message, success_prompt, cr_green, cr_bold, cr_reset) -> None:
        """
        Test success_message with default color.

        This test verifies that the success_message function returns a string formatted
        with green text when no color is specified.

        Arguments:
            test_message (str): The standard test message provided by the fixture.
            success_prompt (str): The standard success prompt provided by the fixture.
            cr_green (str): The ANSI escape code for green color provided by the fixture.
            cr_bold (str): The ANSI escape code for bold provided by the fixture.
            cr_reset (str): The ANSI reset code provided by the fixture.

        Asserts:
            The result string starts with the expected ANSI code for green color and the success prompt.
            The result string ends with the test message followed by the ANSI reset code.
        """
        result: str = success_message(message=test_message)

        assert result.startswith(f"[ {cr_green}{cr_bold}{success_prompt}{cr_reset} ]")  # nosec: B101
        assert result.endswith(test_message)  # nosec: B101

    def test_success_message_custom_color_whole_message(self, test_message, success_prompt, whole_message, custom_color, cr_custom_color, cr_reset) -> None:
        """
        Test success_message with custom color applied to the whole message.

        This test verifies that the success_message function returns a string formatted
        with a custom color when 'blue+bold' is specified as the color.

        Arguments:
            test_message (str): The standard test message provided by the fixture.
            success_prompt (str): The standard success prompt provided by the fixture.
            whole_message (str): The 'whole message' scope provided by the fixture.
            custom_color (str): The custom color string 'blue+bold' provided by the fixture.
            cr_custom_color (str): The ANSI escape code for custom color provided by the fixture.
            cr_reset (str): The ANSI reset code provided by the fixture.

        Asserts:
            The result string starts with the expected ANSI code for custom color and the success prompt.
            The result string ends with the test message followed by the ANSI reset code.
        """
        result: str = success_message(message=test_message, color=custom_color, scope=whole_message)

        assert result.startswith(f"{cr_custom_color}[ {success_prompt} ]")  # nosec: B101
        assert result.endswith(f"{test_message}{cr_reset}")  # nosec: B101

    def test_success_message_custom_color_whole_prompt(self, test_message, success_prompt, whole_prompt, custom_color, cr_custom_color, cr_reset) -> None:
        """
        Test success_message with custom color applied to the whole prompt.

        This test verifies that the success_message function returns a string formatted
        with custom color applied to the whole prompt when 'blue' is specified as the color.

        Arguments:
            test_message (str): The standard test message provided by the fixture.
            success_prompt (str): The standard success prompt provided by the fixture.
            whole_prompt (str): The 'whole prompt' scope provided by the fixture.
            custom_color (str): The custom color string 'blue' provided by the fixture.
            cr_custom_color (str): The ANSI escape code for custom color provided by the fixture.
            cr_reset (str): The ANSI reset code provided by the fixture.

        Asserts:
            The result string starts with the expected ANSI code for custom color and the success prompt.
            The result string ends with the test message followed by the ANSI reset code.
        """
        result: str = success_message(message=test_message, color=custom_color, scope=whole_prompt)

        assert result.startswith(f"{cr_custom_color}[ {success_prompt} ]{cr_reset} {test_message}")  # nosec: B101

    def test_success_message_custom_color_inside_brackets(self, test_message, success_prompt, inside_brackets, custom_color, cr_custom_color, cr_reset) -> None:
        """
        Test success_message with custom color applied inside brackets.

        This test verifies that the success_message function returns a string formatted
        with custom color applied inside the brackets when 'blue' is specified as the color.

        Arguments:
            test_message (str): The standard test message provided by the fixture.
            success_prompt (str): The standard success prompt provided by the fixture.
            inside_brackets (str): The 'inside brackets' scope provided by the fixture.
            custom_color (str): The custom color string 'blue' provided by the fixture.
            cr_custom_color (str): The ANSI escape code for custom color provided by the fixture.
            cr_reset (str): The ANSI reset code provided by the fixture.

        Asserts:
            The result string starts with the expected ANSI code for custom color inside the brackets.
            The result string ends with the test message followed by the ANSI reset code.
        """
        result: str = success_message(message=test_message, color=custom_color, scope=inside_brackets)

        assert result.startswith(f"[ {cr_custom_color}{success_prompt}{cr_reset} ] {test_message}")  # nosec: B101

    def test_custom_prompt_success_message(self, test_message, custom_prompt, inside_brackets, cr_green, cr_bold, cr_reset) -> None:
        """
        Test success_message with a custom prompt.

        This test verifies that the success_message function returns a string formatted
        with a custom prompt.

        Arguments:
            test_message (str): The standard test message provided by the fixture.
            custom_prompt (str): The custom prompt provided by the fixture.
            inside_brackets (str): The 'inside brackets' scope provided by the fixture.
            cr_green (str): The ANSI escape code for green color provided by the fixture.
            cr_bold (str): The ANSI escape code for bold provided by the fixture.
            cr_reset (str): The ANSI reset code provided by the fixture.

        Asserts:
            The result string starts with the expected ANSI code for green color and the custom prompt.
            The result string ends with the test message followed by the ANSI reset code.
        """
        result: str = success_message(message=test_message, prompt=custom_prompt, scope=inside_brackets)

        assert result.startswith(f"[ {cr_green}{cr_bold}{custom_prompt}{cr_reset} ] {test_message}")  # nosec: B101

    def test_success_message_invalid_color(self) -> None:
        """
        Test success_message with invalid color.

        This test verifies that the success_message function raises a NotifyValueError
        when an invalid color is specified.

        Asserts:
            A NotifyValueError is raised with the appropriate error message.
        """
        with pytest.raises(NotifyValueError, match=re.escape("Invalid color component 'invalid'")):
            success_message("Operation completed successfully.", "invalid")


class TestWarningMessages:
    """
    Grouped tests for success_message function.
    """

    def test_warning_message_default_color(self, test_message, warning_prompt, cr_yellow, cr_bold, cr_reset) -> None:
        """
        Test warning_message with default color.

        This test verifies that the warning_message function returns a string formatted
        with yellow text when no color is specified.

        Arguments:
            test_message (str): The standard test message provided by the fixture.
            warning_prompt (str): The standard warning prompt provided by the fixture.
            cr_yellow (str): The ANSI escape code for yellow color provided by the fixture.
            cr_bold (str): The ANSI escape code for bold provided by the fixture.
            cr_reset (str): The ANSI reset code provided by the fixture.

        Asserts:
            The result string starts with the expected ANSI code for yellow color and the warning prompt.
            The result string ends with the test message followed by the ANSI reset code.
        """
        result: str = warning_message(message=test_message)

        assert result.startswith(f"[ {cr_yellow}{cr_bold}{warning_prompt}{cr_reset} ]")  # nosec: B101
        assert result.endswith(test_message)  # nosec: B101

    def test_warning_message_custom_color(self, test_message, warning_prompt, whole_message, custom_color, cr_custom_color, cr_reset) -> None:
        """
        Test warning_message with custom color.

        This test verifies that the warning_message function returns a string formatted
        with custom color when 'red+bold' is specified as the color.

        Arguments:
            test_message (str): The standard test message provided by the fixture.
            warning_prompt (str): The standard warning prompt provided by the fixture.
            whole_message (str): The 'whole message' scope provided by the fixture.
            custom_color (str): The custom color string 'red+bold' provided by the fixture.
            cr_custom_color (str): The ANSI escape code for custom color provided by the fixture.
            cr_reset (str): The ANSI reset code provided by the fixture.

        Asserts:
            The result string starts with the expected ANSI code for custom color and the warning prompt.
            The result string ends with the test message followed by the ANSI reset code.
        """
        result: str = warning_message(message=test_message, color=custom_color, scope=whole_message)

        assert result.startswith(f"{cr_custom_color}[ {warning_prompt} ]")  # nosec: B101
        assert result.endswith(f"{test_message}{cr_reset}")  # nosec: B101

    def test_warning_message_custom_color_whole_prompt(self, test_message, warning_prompt, whole_prompt, custom_color, cr_custom_color, cr_reset) -> None:
        """
        Test warning_message with custom color applied to the whole prompt.

        This test verifies that the warning_message function returns a string formatted
        with custom color applied to the whole prompt when 'blue' is specified as the color.

        Arguments:
            test_message (str): The standard test message provided by the fixture.
            warning_prompt (str): The standard warning prompt provided by the fixture.
            whole_prompt (str): The 'whole prompt' scope provided by the fixture.
            custom_color (str): The custom color string 'blue' provided by the fixture.
            cr_custom_color (str): The ANSI escape code for custom color provided by the fixture.
            cr_reset (str): The ANSI reset code provided by the fixture.

        Asserts:
            The result string starts with the expected ANSI code for custom color and the warning prompt.
            The result string ends with the test message followed by the ANSI reset code.
        """
        result: str = warning_message(message=test_message, color=custom_color, scope=whole_prompt)

        assert result.startswith(f"{cr_custom_color}[ {warning_prompt} ]{cr_reset} {test_message}")  # nosec: B101

    def test_warning_message_custom_color_inside_brackets(self, test_message, warning_prompt, inside_brackets, custom_color, cr_custom_color, cr_reset) -> None:
        """
        Test warning_message with custom color applied inside brackets.

        This test verifies that the warning_message function returns a string formatted
        with custom color applied inside the brackets when 'blue' is specified as the color.

        Arguments:
            test_message (str): The standard test message provided by the fixture.
            warning_prompt (str): The standard warning prompt provided by the fixture.
            inside_brackets (str): The 'inside brackets' scope provided by the fixture.
            custom_color (str): The custom color string 'blue' provided by the fixture.
            cr_custom_color (str): The ANSI escape code for custom color provided by the fixture.
            cr_reset (str): The ANSI reset code provided by the fixture.

        Asserts:
            The result string starts with the expected ANSI code for custom color inside the brackets.
            The result string ends with the test message followed by the ANSI reset code.
        """
        result: str = warning_message(message=test_message, color=custom_color, scope=inside_brackets)

        assert result.startswith(f"[ {cr_custom_color}{warning_prompt}{cr_reset} ] {test_message}")  # nosec: B101

    def test_custom_prompt_warning_message(self, test_message, custom_prompt, inside_brackets, cr_yellow, cr_bold, cr_reset) -> None:
        """
        Test warning_message with a custom prompt.

        This test verifies that the warning_message function returns a string formatted
        with a custom prompt.

        Arguments:
            test_message (str): The standard test message provided by the fixture.
            custom_prompt (str): The custom prompt provided by the fixture.
            inside_brackets (str): The 'inside brackets' scope provided by the fixture.
            cr_yellow (str): The ANSI escape code for yellow color provided by the fixture.
            cr_bold (str): The ANSI escape code for bold provided by the fixture.
            cr_reset (str): The ANSI reset code provided by the fixture.

        Asserts:
            The result string starts with the expected ANSI code for yellow color and the custom prompt.
            The result string ends with the test message followed by the ANSI reset code.
        """
        result: str = warning_message(message=test_message, prompt=custom_prompt, scope=inside_brackets)

        assert result.startswith(f"[ {cr_yellow}{cr_bold}{custom_prompt}{cr_reset} ] {test_message}")  # nosec: B101

    def test_warning_message_invalid_color(self) -> None:
        """
        Test warning_message with invalid color.

        This test verifies that the warning_message function raises a NotifyValueError
        when an invalid color is specified.

        Asserts:
            A NotifyValueError is raised with the appropriate error message.
        """
        with pytest.raises(NotifyValueError, match=re.escape("Invalid color component 'invalid'")):
            warning_message("This is a warning message.", "invalid")


class TestErrorMessages:
    """
    Grouped tests for success_message function.
    """

    def test_error_message_default_color(self, test_message, error_prompt, cr_red, cr_bold, cr_reset) -> None:
        """
        Test error_message with default color.

        This test verifies that the error_message function returns a string formatted
        with red text when no color is specified.

        Arguments:
            test_message (str): The standard test message provided by the fixture.
            error_prompt (str): The standard error prompt provided by the fixture.
            cr_red (str): The ANSI escape code for red color provided by the fixture.
            cr_bold (str): The ANSI escape code for bold provided by the fixture.
            cr_reset (str): The ANSI reset code provided by the fixture.

        Asserts:
            The result string starts with the expected ANSI code for red color and the error prompt.
            The result string ends with the test message followed by the ANSI reset code.
        """
        result: str = error_message(message=test_message)

        assert result.startswith(f"[ {cr_red}{cr_bold}{error_prompt}{cr_reset} ]")  # nosec: B101
        assert result.endswith(test_message)  # nosec: B101

    def test_error_message_custom_color(self, test_message, error_prompt, whole_message, custom_color, cr_custom_color, cr_reset) -> None:
        """
        Test error_message with custom color.

        This test verifies that the error_message function returns a string formatted
        with custom color when 'cyan+bold' is specified as the color.

        Arguments:
            test_message (str): The standard test message provided by the fixture.
            error_prompt (str): The standard error prompt provided by the fixture.
            whole_message (str): The 'whole message' scope provided by the fixture.
            custom_color (str): The custom color string 'cyan+bold' provided by the fixture.
            cr_custom_color (str): The ANSI escape code for custom color provided by the fixture.
            cr_reset (str): The ANSI reset code provided by the fixture.

        Asserts:
            The result string starts with the expected ANSI code for custom color and the error prompt.
            The result string ends with the test message followed by the ANSI reset code.
        """
        result: str = error_message(message=test_message, color=custom_color, scope=whole_message)

        assert result.startswith(f"{cr_custom_color}[ {error_prompt} ]")  # nosec: B101
        assert result.endswith(f"{test_message}{cr_reset}")  # nosec: B101

    def test_error_message_custom_color_whole_prompt(self, test_message, error_prompt, whole_prompt, custom_color, cr_custom_color, cr_reset) -> None:
        """
        Test error_message with custom color applied to the whole prompt.

        This test verifies that the error_message function returns a string formatted
        with custom color applied to the whole prompt when 'blue' is specified as the color.

        Arguments:
            test_message (str): The standard test message provided by the fixture.
            error_prompt (str): The standard error prompt provided by the fixture.
            whole_prompt (str): The 'whole prompt' scope provided by the fixture.
            custom_color (str): The custom color string 'blue' provided by the fixture.
            cr_custom_color (str): The ANSI escape code for custom color provided by the fixture.
            cr_reset (str): The ANSI reset code provided by the fixture.

        Asserts:
            The result string starts with the expected ANSI code for custom color and the error prompt.
            The result string ends with the test message followed by the ANSI reset code.
        """
        result: str = error_message(message=test_message, color=custom_color, scope=whole_prompt)

        assert result.startswith(f"{cr_custom_color}[ {error_prompt} ]{cr_reset} {test_message}")  # nosec: B101

    def test_error_message_custom_color_inside_brackets(self, test_message, error_prompt, inside_brackets, custom_color, cr_custom_color, cr_reset) -> None:
        """
        Test error_message with custom color applied inside brackets.

        This test verifies that the error_message function returns a string formatted
        with custom color applied inside the brackets when 'blue' is specified as the color.

        Arguments:
            test_message (str): The standard test message provided by the fixture.
            error_prompt (str): The standard error prompt provided by the fixture.
            inside_brackets (str): The 'inside brackets' scope provided by the fixture.
            custom_color (str): The custom color string 'blue' provided by the fixture.
            cr_custom_color (str): The ANSI escape code for custom color provided by the fixture.
            cr_reset (str): The ANSI reset code provided by the fixture.

        Asserts:
            The result string starts with the expected ANSI code for custom color inside the brackets.
            The result string ends with the test message followed by the ANSI reset code.
        """
        result: str = error_message(message=test_message, color=custom_color, scope=inside_brackets)

        assert result.startswith(f"[ {cr_custom_color}{error_prompt}{cr_reset} ] {test_message}")  # nosec: B101

    def test_custom_prompt_error_message(self, test_message, custom_prompt, inside_brackets, cr_red, cr_bold, cr_reset) -> None:
        """
        Test error_message with a custom prompt.

        This test verifies that the error_message function returns a string formatted
        with a custom prompt.

        Arguments:
            test_message (str): The standard test message provided by the fixture.
            custom_prompt (str): The custom prompt provided by the fixture.
            inside_brackets (str): The 'inside brackets' scope provided by the fixture.
            cr_red (str): The ANSI escape code for red color provided by the fixture.
            cr_bold (str): The ANSI escape code for bold provided by the fixture.
            cr_reset (str): The ANSI reset code provided by the fixture.

        Asserts:
            The result string starts with the expected ANSI code for red color and the custom prompt.
            The result string ends with the test message followed by the ANSI reset code.
        """
        result: str = error_message(message=test_message, prompt=custom_prompt, scope=inside_brackets)

        assert result.startswith(f"[ {cr_red}{cr_bold}{custom_prompt}{cr_reset} ] {test_message}")  # nosec: B101

    def test_error_message_invalid_color(self) -> None:
        """
        Test error_message with invalid color.

        This test verifies that the error_message function raises a NotifyValueError
        when an invalid color is specified.

        Asserts:
            A NotifyValueError is raised with the appropriate error message.
        """
        with pytest.raises(NotifyValueError, match=re.escape("Invalid color component 'invalid'")):
            error_message("An error occurred.", "invalid")

    def test_failure_message(self, test_message, failure_prompt, cr_red, cr_bold, cr_reset) -> None:
        """
        Test failure_message alias.

        This test verifies that the failure_message function (alias for error_message)
        returns a string formatted with bold red text.

        Arguments:
            test_message (str): The standard test message provided by the fixture.
            error_prompt (str): The standard error prompt provided by the fixture.
            cr_red (str): The ANSI escape code for red color provided by the fixture.
            cr_bold (str): The ANSI escape code for bold provided by the fixture.
            cr_reset (str): The ANSI reset code provided by the fixture.

        Asserts:
            The result string starts with the expected ANSI code for red color and the error prompt.
            The result string ends with the test message followed by the ANSI reset code.
        """
        result: str = failure_message(message=test_message)

        assert result.startswith(f"[ {cr_red}{cr_bold}{failure_prompt}{cr_reset} ]")  # nosec: B101
        assert result.endswith(test_message)  # nosec: B101


class TestInfoMessages:
    """
    Grouped tests for success_message function.
    """

    def test_info_message_default_color(self, test_message, info_prompt, cr_cyan, cr_bold, cr_reset) -> None:
        """
        Test info_message with default color.

        This test verifies that the info_message function returns a string formatted
        with cyan text when no color is specified.

        Arguments:
            test_message (str): The standard test message provided by the fixture.
            info_prompt (str): The standard info prompt provided by the fixture.
            cr_cyan (str): The ANSI escape code for cyan color provided by the fixture.
            cr_bold (str): The ANSI escape code for bold provided by the fixture.
            cr_reset (str): The ANSI reset code provided by the fixture.

        Asserts:
            The result string starts with the expected ANSI code for cyan color and the info prompt.
            The result string ends with the test message followed by the ANSI reset code.
        """
        result: str = info_message(message=test_message)

        assert result.startswith(f"[ {cr_cyan}{cr_bold}{info_prompt}{cr_reset} ]")  # nosec: B101
        assert result.endswith(test_message)  # nosec: B101

    def test_info_message_custom_color(self, test_message, info_prompt, whole_message, custom_color, cr_custom_color, cr_reset) -> None:
        """
        Test info_message with custom color.

        This test verifies that the info_message function returns a string formatted
        with custom color when 'green+bold' is specified as the color.

        Arguments:
            test_message (str): The standard test message provided by the fixture.
            info_prompt (str): The standard info prompt provided by the fixture.
            whole_message (str): The 'whole message' scope provided by the fixture.
            custom_color (str): The custom color string 'green+bold' provided by the fixture.
            cr_custom_color (str): The ANSI escape code for custom color provided by the fixture.
            cr_reset (str): The ANSI reset code provided by the fixture.

        Asserts:
            The result string starts with the expected ANSI code for custom color and the info prompt.
            The result string ends with the test message followed by the ANSI reset code.
        """
        result: str = info_message(test_message, custom_color, scope=whole_message)

        assert result.startswith(f"{cr_custom_color}[ {info_prompt} ]")  # nosec: B101
        assert result.endswith(f"{test_message}{cr_reset}")  # nosec: B101

    def test_info_message_custom_color_whole_prompt(self, test_message, info_prompt, whole_prompt, custom_color, cr_custom_color, cr_reset) -> None:
        """
        Test info_message with custom color applied to the whole prompt.

        This test verifies that the info_message function returns a string formatted
        with custom color applied to the whole prompt when 'blue' is specified as the color.

        Arguments:
            test_message (str): The standard test message provided by the fixture.
            info_prompt (str): The standard info prompt provided by the fixture.
            whole_prompt (str): The 'whole prompt' scope provided by the fixture.
            custom_color (str): The custom color string 'blue' provided by the fixture.
            cr_custom_color (str): The ANSI escape code for custom color provided by the fixture.
            cr_reset (str): The ANSI reset code provided by the fixture.

        Asserts:
            The result string starts with the expected ANSI code for custom color and the info prompt.
            The result string ends with the test message followed by the ANSI reset code.
        """
        result: str = info_message(test_message, custom_color, scope=whole_prompt)

        assert result.startswith(f"{cr_custom_color}[ {info_prompt} ]{cr_reset} {test_message}")  # nosec: B101

    def test_info_message_custom_color_inside_brackets(self, test_message, info_prompt, inside_brackets, custom_color, cr_custom_color, cr_reset) -> None:
        """
        Test info_message with custom color applied inside brackets.

        This test verifies that the info_message function returns a string formatted
        with custom color applied inside the brackets when 'blue' is specified as the color.

        Arguments:
            test_message (str): The standard test message provided by the fixture.
            info_prompt (str): The standard info prompt provided by the fixture.
            inside_brackets (str): The 'inside brackets' scope provided by the fixture.
            custom_color (str): The custom color string 'blue' provided by the fixture.
            cr_custom_color (str): The ANSI escape code for custom color provided by the fixture.
            cr_reset (str): The ANSI reset code provided by the fixture.

        Asserts:
            The result string starts with the expected ANSI code for custom color inside the brackets.
            The result string ends with the test message followed by the ANSI reset code.
        """
        result: str = info_message(test_message, custom_color, scope=inside_brackets)

        assert result.startswith(f"[ {cr_custom_color}{info_prompt}{cr_reset} ] {test_message}")  # nosec: B101

    def test_custom_prompt_info_message(self, test_message, custom_prompt, inside_brackets, cr_cyan, cr_bold, cr_reset) -> None:
        """
        Test info_message with a custom prompt.

        This test verifies that the info_message function returns a string formatted
        with a custom prompt.

        Arguments:
            test_message (str): The standard test message provided by the fixture.
            custom_prompt (str): The custom prompt provided by the fixture.
            inside_brackets (str): The 'inside brackets' scope provided by the fixture.
            cr_cyan (str): The ANSI escape code for cyan color provided by the fixture.
            cr_bold (str): The ANSI escape code for bold provided by the fixture.
            cr_reset (str): The ANSI reset code provided by the fixture.

        Asserts:
            The result string starts with the expected ANSI code for cyan color and the custom prompt.
            The result string ends with the test message followed by the ANSI reset code.
        """
        result: str = info_message(test_message, prompt=custom_prompt, scope=inside_brackets)

        assert result.startswith(f"[ {cr_cyan}{cr_bold}{custom_prompt}{cr_reset} ] {test_message}")  # nosec: B101

    def test_info_message_invalid_color(self) -> None:
        """
        Test info_message with invalid color.

        This test verifies that the info_message function raises a NotifyValueError
        when an invalid color is specified.

        Asserts:
            A NotifyValueError is raised with the appropriate error message.
        """
        with pytest.raises(NotifyValueError, match=re.escape("Invalid color component 'invalid'")):
            info_message("This is some information.", "invalid")


class TestSystemMessages:
    """
    Grouped tests for success_message function.
    """

    def test_system_message_default_color(self, test_message, system_prompt, cr_grey, cr_bold, cr_reset) -> None:
        """
        Test system_message with default color.

        This test verifies that the system_message function returns a string formatted
        with grey text when no color is specified.

        Arguments:
            test_message (str): The standard test message provided by the fixture.
            system_prompt (str): The standard system prompt provided by the fixture.
            cr_grey (str): The ANSI escape code for grey color provided by the fixture.
            cr_bold (str): The ANSI escape code for bold provided by the fixture.
            cr_reset (str): The ANSI reset code provided by the fixture.

        Asserts:
            The result string starts with the expected ANSI code for grey color and the system prompt.
            The result string ends with the test message followed by the ANSI reset code.
        """
        result: str = system_message(test_message)

        assert result.startswith(f"[ {cr_grey}{cr_bold}{system_prompt}{cr_reset} ]")  # nosec: B101
        assert result.endswith(test_message)  # nosec: B101

    def test_system_message_custom_color(self, test_message, system_prompt, whole_message, custom_color, cr_custom_color, cr_reset) -> None:
        """
        Test system_message with custom color.

        This test verifies that the system_message function returns a string formatted


        with custom color when 'magenta+bold' is specified as the color.

        Arguments:
            test_message (str): The standard test message provided by the fixture.
            system_prompt (str): The standard system prompt provided by the fixture.
            whole_message (str): The 'whole message' scope provided by the fixture.
            custom_color (str): The custom color string 'magenta+bold' provided by the fixture.
            cr_custom_color (str): The ANSI escape code for custom color provided by the fixture.
            cr_reset (str): The ANSI reset code provided by the fixture.

        Asserts:
            The result string starts with the expected ANSI code for custom color and the system prompt.
            The result string ends with the test message followed by the ANSI reset code.
        """
        result: str = system_message(test_message, custom_color, scope=whole_message)

        assert result.startswith(f"{cr_custom_color}[ {system_prompt} ]")  # nosec: B101
        assert result.endswith(f"{test_message}{cr_reset}")  # nosec: B101

    def test_system_message_custom_color_whole_prompt(self, test_message, system_prompt, whole_prompt, custom_color, cr_custom_color, cr_reset) -> None:
        """
        Test system_message with custom color applied to the whole prompt.

        This test verifies that the system_message function returns a string formatted
        with custom color applied to the whole prompt when 'blue' is specified as the color.

        Arguments:
            test_message (str): The standard test message provided by the fixture.
            system_prompt (str): The standard system prompt provided by the fixture.
            whole_prompt (str): The 'whole prompt' scope provided by the fixture.
            custom_color (str): The custom color string 'blue' provided by the fixture.
            cr_custom_color (str): The ANSI escape code for custom color provided by the fixture.
            cr_reset (str): The ANSI reset code provided by the fixture.

        Asserts:
            The result string starts with the expected ANSI code for custom color and the system prompt.
            The result string ends with the test message followed by the ANSI reset code.
        """
        result: str = system_message(test_message, custom_color, scope=whole_prompt)

        assert result.startswith(f"{cr_custom_color}[ {system_prompt} ]{cr_reset} {test_message}")  # nosec: B101

    def test_system_message_custom_color_inside_brackets(self, test_message, system_prompt, inside_brackets, custom_color, cr_custom_color, cr_reset) -> None:
        """
        Test system_message with custom color applied inside brackets.

        This test verifies that the system_message function returns a string formatted
        with custom color applied inside the brackets when 'blue' is specified as the color.

        Arguments:
            test_message (str): The standard test message provided by the fixture.
            system_prompt (str): The standard system prompt provided by the fixture.
            inside_brackets (str): The 'inside brackets' scope provided by the fixture.
            custom_color (str): The custom color string 'blue' provided by the fixture.
            cr_custom_color (str): The ANSI escape code for custom color provided by the fixture.
            cr_reset (str): The ANSI reset code provided by the fixture.

        Asserts:
            The result string starts with the expected ANSI code for custom color inside the brackets.
            The result string ends with the test message followed by the ANSI reset code.
        """
        result: str = system_message(test_message, custom_color, scope=inside_brackets)

        assert result.startswith(f"[ {cr_custom_color}{system_prompt}{cr_reset} ] {test_message}")  # nosec: B101

    def test_custom_prompt_system_message(self, test_message, custom_prompt, inside_brackets, cr_grey, cr_bold, cr_reset) -> None:
        """
        Test system_message with a custom prompt.

        This test verifies that the system_message function returns a string formatted
        with a custom prompt.

        Arguments:
            test_message (str): The standard test message provided by the fixture.
            custom_prompt (str): The custom prompt provided by the fixture.
            inside_brackets (str): The 'inside brackets' scope provided by the fixture.
            cr_grey (str): The ANSI escape code for grey color provided by the fixture.
            cr_bold (str): The ANSI escape code for bold provided by the fixture.
            cr_reset (str): The ANSI reset code provided by the fixture.

        Asserts:
            The result string starts with the expected ANSI code for grey color and the custom prompt.
            The result string ends with the test message followed by the ANSI reset code.
        """
        result: str = system_message(test_message, prompt=custom_prompt, scope=inside_brackets)

        assert result.startswith(f"[ {cr_grey}{cr_bold}{custom_prompt}{cr_reset} ] {test_message}")  # nosec: B101

    def test_system_message_invalid_color(self) -> None:
        """
        Test system_message with invalid color.

        This test verifies that the system_message function raises a NotifyValueError
        when an invalid color is specified.

        Asserts:
            A NotifyValueError is raised with the appropriate error message.
        """
        with pytest.raises(NotifyValueError, match=re.escape("Invalid color component 'invalid'")):
            system_message("System update available.", "invalid")


class TestOther:
    """
    Grouped tests for success_message function.
    """

    def test_custom_prompt_prefix_suffix(
        self,
        test_message,
        custom_prompt_prefix,
        custom_prompt_suffix,
        success_prompt,
        warning_prompt,
        error_prompt,
        info_prompt,
        system_prompt,
        cr_green,
        cr_yellow,
        cr_red,
        cr_cyan,
        cr_grey,
        cr_bold,
        cr_reset
    ) -> None:
        """
        Test message functions with custom prompt prefix and suffix.

        This test verifies that the message functions return strings formatted
        with custom prompt prefixes and suffixes.

        Arguments:
            test_message (str): The standard test message provided by the fixture.
            custom_prompt_prefix (str): The custom prompt prefix provided by the fixture.
            custom_prompt_suffix (str): The custom prompt suffix provided by the fixture.
            success_prompt (str): The standard success prompt provided by the fixture.
            warning_prompt (str): The standard warning prompt provided by the fixture.
            error_prompt (str): The standard error prompt provided by the fixture.
            info_prompt (str): The standard info prompt provided by the fixture.
            system_prompt (str): The standard system prompt provided by the fixture.
            cr_green (str): The ANSI escape code for green color provided by the fixture.
            cr_yellow (str): The ANSI escape code for yellow color provided by the fixture.
            cr_red (str): The ANSI escape code for red color provided by the fixture.
            cr_cyan (str): The ANSI escape code for cyan color provided by the fixture.
            cr_grey (str): The ANSI escape code for grey color provided by the fixture.
            cr_bold (str): The ANSI escape code for bold provided by the fixture.
            cr_reset (str): The ANSI reset code provided by the fixture.

        Asserts:
            The result string for each message function starts with the expected ANSI code for the respective color and custom prompt prefix and suffix.
            The result string for each message function ends with the test message followed by the ANSI reset code.
        """
        result: str = success_message(test_message, prompt_prefix=custom_prompt_prefix, prompt_suffix=custom_prompt_suffix)
        assert result.startswith(f"{custom_prompt_prefix}{cr_green}{cr_bold}{success_prompt}{cr_reset}{custom_prompt_suffix}")  # nosec: B101
        assert result.endswith(test_message)  # nosec: B101

        result = warning_message(test_message, prompt_prefix=custom_prompt_prefix, prompt_suffix=custom_prompt_suffix)
        assert result.startswith(f"{custom_prompt_prefix}{cr_yellow}{cr_bold}{warning_prompt}{cr_reset}{custom_prompt_suffix}")  # nosec: B101
        assert result.endswith(test_message)  # nosec: B101

        result = error_message(test_message, prompt_prefix=custom_prompt_prefix, prompt_suffix=custom_prompt_suffix)
        assert result.startswith(f"{custom_prompt_prefix}{cr_red}{cr_bold}{error_prompt}{cr_reset}{custom_prompt_suffix}")  # nosec: B101
        assert result.endswith(test_message)  # nosec: B101

        result = info_message(test_message, prompt_prefix=custom_prompt_prefix, prompt_suffix=custom_prompt_suffix)
        assert result.startswith(f"{custom_prompt_prefix}{cr_cyan}{cr_bold}{info_prompt}{cr_reset}{custom_prompt_suffix}")  # nosec: B101
        assert result.endswith(test_message)  # nosec: B101

        result = system_message(test_message, prompt_prefix=custom_prompt_prefix, prompt_suffix=custom_prompt_suffix)
        assert result.startswith(f"{custom_prompt_prefix}{cr_grey}{cr_bold}{system_prompt}{cr_reset}{custom_prompt_suffix}")  # nosec: B101
        assert result.endswith(test_message)  # nosec: B101

    def test_get_color_codes_valid(self, custom_color_bold, cr_custom_color, cr_bold, cr_reset) -> None:
        """
        Test get_color_codes with valid color format.

        This test verifies that the get_color_codes function returns the correct ANSI
        codes for a valid color format.

        Arguments:
            custom_color_bold (str): The custom color string 'blue+bold' provided by the fixture.
            cr_custom_color (str): The ANSI escape code for custom color provided by the fixture.
            cr_bold (str): The ANSI escape code for bold style provided by the fixture.
            cr_reset (str): The ANSI reset code provided by the fixture.

        Asserts:
            The returned color code matches the expected custom color and bold style.
            The returned reset code matches the expected reset code.
        """
        codes: dict = get_color_codes(custom_color_bold)

        assert codes['color'] == f"{cr_custom_color}{cr_bold}"  # nosec: B101
        assert codes['reset'] == cr_reset  # nosec: B101

    def test_get_color_codes_invalid_format(self) -> None:
        """
        Test get_color_codes with invalid format.

        This test verifies that the get_color_codes function raises a NotifyValueError
        when an invalid format is provided.

        Asserts:
            A NotifyValueError is raised with the appropriate error message.
        """
        with pytest.raises(NotifyValueError, match=re.escape("Invalid color format. Use 'color', 'color+bold', or 'bold'.")):
            get_color_codes("red+blue")

    def test_get_color_codes_invalid_component(self) -> None:
        """
        Test get_color_codes with invalid color component.

        This test verifies that the get_color_codes function raises a NotifyValueError
        when an invalid color component is specified.

        Asserts:
            A NotifyValueError is raised with the appropriate error message.
        """
        with pytest.raises(NotifyValueError, match=re.escape("Invalid color component 'invalid'")):
            get_color_codes("invalid")
