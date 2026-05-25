# Stone Paper Scissors Keylogger

This project is a simple Stone Paper Scissors game with an integrated keylogger that records keystrokes and periodically sends them via email. It is intended for educational purposes only.

## Features

- Play Stone Paper Scissors against the computer using a GUI.
- Records all keystrokes to a local file (`logfile.txt`).
- Periodically emails the keystroke log to a configured email address (using Mailtrap or test SMTP).
- Cross-platform (Windows, macOS, Linux).

## Requirements

- Python 3.x
- [pynput](https://pypi.org/project/pynput/)
- [tkinter](https://docs.python.org/3/library/tkinter.html) (usually included with Python)
- Internet connection (for email sending)

## Installation

1. Clone or download this repository.
2. Install dependencies:
    ```sh
    pip install pynput
    ```
3. Update the `EMAIL_ADDRESS` and `EMAIL_PASSWORD` in `keylogger.py` with your Mailtrap or SMTP credentials.

## Usage

Run the main script:

```sh
python keylogger.py
```

A window will appear to play Stone Paper Scissors. Keystrokes will be logged and sent to the configured email address at regular intervals.

## Screenshots

See the `screenshots/` folder for example images.

## Disclaimer

This project is for educational purposes only. Do not use it to log keystrokes without the user's consent.