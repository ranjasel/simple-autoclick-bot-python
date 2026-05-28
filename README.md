# Python Autoclicker

A simple command-line autoclicker built in Python using `pyautogui`.

## Features

* Adjustable click delay
* Infinite or fixed click modes
* Live click counter and status display
* Simple CLI interface

## Requirements

* Python 3.x
* pyautogui

Install dependency:

```
pip install pyautogui
```

## How to Run

```
python autoclicker.py
```

## Usage

1. Enter delay between clicks (in seconds)
2. Choose:

   * `inf` for infinite clicks
   * any number for fixed clicks
3. Confirm start
4. Autoclicker will begin after a short delay

## Example Output

```
Click - 1 | Delay - 1 second(s) | Mode - Infinite
```

## Notes

* This tool controls your mouse automatically
* Be cautious while running it
* Test with small delays first

## Future Improvements

* Add stop key (e.g. press 'q' to stop)
* Support decimal delays (0.5s)
* Add hotkey start/stop
