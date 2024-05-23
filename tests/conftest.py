"""
This configuration module for pytest defines fixtures that are used across multiple test files.

Fixtures:
---------
- `test_message`: Provides a standard test message for use in various tests.
- `success_prompt`: Provides a standard success prompt for use in various tests.
- `warning_prompt`: Provides a standard warning prompt for use in various tests.
- `error_prompt`: Provides a standard error prompt for use in various tests.
- `failure_prompt`: Provides a standard failure prompt for use in various tests.
- `info_prompt`: Provides a standard info prompt for use in various tests.
- `system_prompt`: Provides a standard system prompt for use in various tests.
- `custom_prompt`: Provides a standard custom prompt for use in various tests.
- `custom_prompt_prefix`: Provides a standard custom prompt prefix for use in various tests.
- `custom_prompt_suffix`: Provides a standard custom prompt suffix for use in various tests.
- `custom_color`: Provides a standard test color for use in various tests.
- `cr_custom_color`: Provides the colorama.Fore.XXX color code for custom color.
- `cr_red`: Provides the colorama.Fore.RED color code.
- `cr_yellow`: Provides the colorama.Fore.YELLOW color code.
- `cr_green`: Provides the colorama.Fore.GREEN color code.
- `cr_cyan`: Provides the colorama.Fore.CYAN color code.
- `cr_grey`: Provides the colorama.Fore.LIGHTBLACK_EX color code.
- `cr_bold`: Provides the colorama.Style.BRIGHT color code.
- `cr_reset`: Provides the colorama.Style.RESET_ALL color code.
- `custom_color_bold`: Provides a standard test color with bold style for use in various tests.
- `default_scope`: Provides a default scope for use in various tests.
- `whole_message`: Provides a 'whole message' scope for use in various tests.
- `whole_prompt`: Provides a 'whole prompt' scope for use in various tests.
- `inside_brackets`: Provides a 'inside brackets' scope for use in various tests.

These fixtures are defined with a session scope, meaning they are initialized once per test session
and can be used by any test function within that session.

Example Usage:
--------------
To use these fixtures in your test functions, simply add them as parameters to your test function definitions:

    def test_example(test_message, success_prompt):
        assert success_message(test_message, prompt=success_prompt) == "expected result"

This ensures that the same test message and prompts are used consistently across all tests.
"""

from typing import Literal
import pytest
import colorama


@pytest.fixture(scope="session")
def test_message() -> Literal['This is a message']:
    """
    Provide a standard test message.

    This fixture returns a string that can be used as a standard test message
    across multiple tests.

    Returns:
        str: A standard test message.
    """
    return "This is a message"


@pytest.fixture(scope="session")
def success_prompt() -> Literal['Success']:
    """
    Provide a standard success prompt.

    This fixture returns a string that can be used as a standard success prompt
    across multiple tests.

    Returns:
        str: A standard success prompt.
    """
    return "Success"


@pytest.fixture(scope="session")
def warning_prompt() -> Literal['Warning']:
    """
    Provide a standard warning prompt.

    This fixture returns a string that can be used as a standard warning prompt
    across multiple tests.

    Returns:
        str: A standard warning prompt.
    """
    return "Warning"


@pytest.fixture(scope="session")
def error_prompt() -> Literal['Error']:
    """
    Provide a standard error prompt.

    This fixture returns a string that can be used as a standard error prompt
    across multiple tests.

    Returns:
        str: A standard error prompt.
    """
    return "Error"


@pytest.fixture(scope="session")
def failure_prompt() -> Literal['Failure']:
    """
    Provide a standard failure prompt.

    This fixture returns a string that can be used as a standard failure prompt
    across multiple tests.

    Returns:
        str: A standard error prompt.
    """
    return "Failure"


@pytest.fixture(scope="session")
def info_prompt() -> Literal['Info']:
    """
    Provide a standard info prompt.

    This fixture returns a string that can be used as a standard info prompt
    across multiple tests.

    Returns:
        str: A standard info prompt.
    """
    return "Info"


@pytest.fixture(scope="session")
def system_prompt() -> Literal['System']:
    """
    Provide a standard system prompt.

    This fixture returns a string that can be used as a standard system prompt
    across multiple tests.

    Returns:
        str: A standard system prompt.
    """
    return "System"


@pytest.fixture(scope="session")
def custom_prompt() -> Literal['Custom']:
    """
    Provide a standard custom prompt.

    This fixture returns a string that can be used as a standard custom prompt
    across multiple tests.

    Returns:
        str: A standard custom prompt.
    """
    return "Custom"


@pytest.fixture(scope="session")
def custom_prompt_prefix() -> Literal['{ ']:
    """
    Provide a standard custom prompt prefix.

    This fixture returns a string that can be used as a standard custom prompt
    prefix across multiple tests.

    Returns:
        str: A standard custom prompt prefix.
    """
    return "{ "


@pytest.fixture(scope="session")
def custom_prompt_suffix() -> Literal[' }']:
    """
    Provide a standard custom prompt suffix.

    This fixture returns a string that can be used as a standard custom prompt
    suffix across multiple tests.

    Returns:
        str: A standard custom prompt suffix.
    """
    return " }"


@pytest.fixture(scope="session")
def custom_color() -> Literal['blue']:
    """
    Provide a standard test color.

    This fixture returns a string that can be used as the default test color
    across multiple tests.

    Returns:
        str: The default test color.
    """
    return "blue"


@pytest.fixture
def cr_custom_color() -> str:
    """
    Provide the colorama.Fore.XXX color code.

    Returns:
        str: The ANSI escape code for custom color.
    """
    return colorama.Fore.BLUE


@pytest.fixture
def cr_red() -> str:
    """
    Provide the colorama.Fore.RED color code.

    Returns:
        str: The ANSI escape code for red text.
    """
    return colorama.Fore.RED


@pytest.fixture
def cr_yellow() -> str:
    """
    Provide the colorama.Fore.YELLOW color code.

    Returns:
        str: The ANSI escape code for yellow text.
    """
    return colorama.Fore.YELLOW


@pytest.fixture
def cr_green() -> str:
    """
    Provide the colorama.Fore.GREEN color code.

    Returns:
        str: The ANSI escape code for green text.
    """
    return colorama.Fore.GREEN


@pytest.fixture
def cr_cyan() -> str:
    """
    Provide the colorama.Fore.CYAN color code.

    Returns:
        str: The ANSI escape code for cyan text.
    """
    return colorama.Fore.CYAN


@pytest.fixture
def cr_grey() -> str:
    """
    Provide the colorama.Fore.LIGHTBLACK_EX (grey) color code.

    Returns:
        str: The ANSI escape code for grey text.
    """
    return colorama.Fore.LIGHTBLACK_EX


@pytest.fixture
def cr_bold() -> str:
    """
    Provide the colorama.Style.BRIGHT color code.

    Returns:
        str: The ANSI escape code for bold color.
    """
    return colorama.Style.BRIGHT


@pytest.fixture
def cr_reset() -> str:
    """
    Provide the colorama.Style.RESET_ALL color code.

    Returns:
        str: The ANSI escape code for resetting color.
    """
    return colorama.Style.RESET_ALL


@pytest.fixture(scope="session")
def custom_color_bold() -> Literal['blue+bold']:
    """
    Provide a standard test color.

    This fixture returns a string that can be used as the default test color
    across multiple tests.

    Returns:
        str: The default test color + bold.
    """
    return "blue+bold"


@pytest.fixture(scope="session")
def default_scope() -> Literal['prompt_text']:
    """
    Provide a default scope.

    This fixture returns a string that can be used as the default scope
    across multiple tests.

    Returns:
        str: The default scope.
    """
    return "prompt_text"


@pytest.fixture(scope="session")
def whole_message() -> Literal['all']:
    """
    Provide a 'all' scope.

    This fixture returns a string that can be used across multiple tests.

    Returns:
        str: The default scope.
    """
    return "all"


@pytest.fixture(scope="session")
def whole_prompt() -> Literal['prompt']:
    """
    Provide a 'prompt' scope.

    This fixture returns a string that can be used across multiple tests.

    Returns:
        str: The default scope.
    """
    return "prompt"


@pytest.fixture(scope="session")
def inside_brackets() -> Literal['prompt_text']:
    """
    Provide a 'prompt_text' scope.

    This fixture returns a string that can be used across multiple tests.

    Returns:
        str: The default scope.
    """
    return "prompt_text"
