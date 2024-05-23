<!-- markdownlint-disable -->
<p align="center">
    <a href="https://github.com/DevelopersToolbox/">
        <img src="https://cdn.wolfsoftware.com/assets/images/github/organisations/developerstoolbox/black-and-white-circle-256.png" alt="DevelopersToolbox logo" />
    </a>
    <br />
    <a href="https://github.com/DevelopersToolbox/notify-package/actions/workflows/cicd.yml">
        <img src="https://img.shields.io/github/actions/workflow/status/DevelopersToolbox/notify-package/cicd.yml?branch=master&label=build%20status&style=for-the-badge" alt="Github Build Status" />
    </a>
    <a href="https://github.com/DevelopersToolbox/notify-package/blob/master/LICENSE.md">
        <img src="https://img.shields.io/github/license/DevelopersToolbox/notify-package?color=blue&label=License&style=for-the-badge" alt="License">
    </a>
    <a href="https://github.com/DevelopersToolbox/notify-package">
        <img src="https://img.shields.io/github/created-at/DevelopersToolbox/notify-package?color=blue&label=Created&style=for-the-badge" alt="Created">
    </a>
    <br />
    <a href="https://github.com/DevelopersToolbox/notify-package/releases/latest">
        <img src="https://img.shields.io/github/v/release/DevelopersToolbox/notify-package?color=blue&label=Latest%20Release&style=for-the-badge" alt="Release">
    </a>
    <a href="https://github.com/DevelopersToolbox/notify-package/releases/latest">
        <img src="https://img.shields.io/github/release-date/DevelopersToolbox/notify-package?color=blue&label=Released&style=for-the-badge" alt="Released">
    </a>
    <a href="https://github.com/DevelopersToolbox/notify-package/releases/latest">
        <img src="https://img.shields.io/github/commits-since/DevelopersToolbox/notify-package/latest.svg?color=blue&style=for-the-badge" alt="Commits since release">
    </a>
    <br />
    <a href="https://github.com/DevelopersToolbox/notify-package/blob/master/.github/CODE_OF_CONDUCT.md">
        <img src="https://img.shields.io/badge/Code%20of%20Conduct-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/DevelopersToolbox/notify-package/blob/master/.github/CONTRIBUTING.md">
        <img src="https://img.shields.io/badge/Contributing-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/DevelopersToolbox/notify-package/blob/master/.github/SECURITY.md">
        <img src="https://img.shields.io/badge/Report%20Security%20Concern-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/DevelopersToolbox/notify-package/issues">
        <img src="https://img.shields.io/badge/Get%20Support-blue?style=for-the-badge" />
    </a>
</p>

## Overview

The Notify package provides a set of utility functions for printing formatted messages to the terminal. The main purpose of this
module is to facilitate the display of success, warning, error, informational, and system messages with specific color and style
formatting using predefined constants.

## Features

- Display success messages with green text.
- Display warning messages with yellow text.
- Display error messages with red text.
- Display informational messages with cyan text.
- Display system messages with grey text.
- Support for custom colors, prompts, and formatting scopes.
- Error handling for invalid colors and scopes.

## Installation

To install the Notify package, use the following command:

```bash
pip install wolfsoftware.notify
```

## Usage

Here is an example of how to use the notification functions provided by the Notify package:

```python
from wolfsoftware.notify import success_message, warning_message, error_message, info_message, system_message

print(success_message("Operation completed successfully."))
print(warning_message("This is a warning message."))
print(error_message("An error occurred."))
print(info_message("This is some information."))
print(system_message("System update available."))
```

## Functions

### `success_message`

Print a success message with a specific format.

```python
def success_message(
        message: str,
        color: str = 'green+bold',
        prompt: str = 'Success',
        scope: str = 'prompt_text',
        prompt_prefix: str = '[ ',
        prompt_suffix: str = ' ]'
    ) -> str:
```

### `warning_message`

Print a warning message with a specific format.

```python
def warning_message(
        message: str,
        color: str = 'yellow+bold',
        prompt: str = 'Warning',
        scope: str = 'prompt_text',
        prompt_prefix: str = '[ ',
        prompt_suffix: str = ' ]'
    ) -> str:
```

### `error_message`

Print an error message with a specific format.

```python
def error_message(
        message: str,
        color: str = 'red+bold',
        prompt: str = 'Error',
        scope: str = 'prompt_text',
        prompt_prefix: str = '[ ',
        prompt_suffix: str = ' ]'
    ) -> str:
```

### `failure_message`

Alias for `error_message`, but with a prompt='Failure'.

```python
failure_message = error_message
```

### `info_message`

Print an informational message with a specific format.

```python
def info_message(
        message: str,
        color: str = 'cyan+bold',
        prompt: str = 'Info',
        scope: str = 'prompt_text',
        prompt_prefix: str = '[ ',
        prompt_suffix: str = ' ]'
    ) -> str:
```

### `system_message`

Print a system message with a specific format.

```python
def system_message(
        message: str,
        color: str = 'grey+bold',
        prompt: str = 'System',
        scope: str = 'prompt_text',
        prompt_prefix: str = '[ ',
        prompt_suffix: str = ' ]'
    ) -> str:
```

## Customization

You can customize the color, prompt text, and the scope of the color application using the provided parameters. Here are some examples:

### Custom Colors

```python
print(success_message("Operation completed successfully.", color="blue+bold"))
```

### Custom Prompts

```python
print(success_message("Operation completed successfully.", prompt="Completed"))
```

### Custom Scopes

- `all`: Applies the color to the entire message.
- `prompt`: Applies the color to the prompt only.
- `prompt_text`: Applies the color to the text inside the brackets.

```python
print(success_message("Operation completed successfully.", scope="prompt"))
print(success_message("Operation completed successfully.", scope="prompt_text"))
```

### Custom Prefixes and Suffixes

You can also customize the prompt prefix and suffix.

```python
print(success_message("Operation completed successfully.", prompt_prefix="<<", prompt_suffix=">>"))
```

## Error Handling

The Notify package includes error handling for invalid color and scope inputs. If an invalid color or scope is provided, a `NotifyValueError` will be raised with an appropriate error message.

```python
from wolfsoftware.notify import NotifyValueError

try:
    print(success_message("Operation completed successfully.", color="invalid"))
except NotifyValueError as e:
    print(f"Error: {e}")
```

## Testing

The Notify package includes a comprehensive test suite to ensure the correct functionality of all message formatting functions. The tests verify that the package version is defined, the message functions return correctly formatted strings, and exceptions are raised appropriately for invalid inputs.

### Running Tests

To run the tests, use a testing framework such as pytest:

```bash
pytest tests/test_notify.py
```

## Acknowledgements

The Notify package uses the `colorama` library for cross-platform support of ANSI color codes. Many thanks to the contributors of the `colorama` project for their excellent work.

<br />
<p align="right"><a href="https://wolfsoftware.com/"><img src="https://img.shields.io/badge/Created%20by%20Wolf%20on%20behalf%20of%20Wolf%20Software-blue?style=for-the-badge" /></a></p>
