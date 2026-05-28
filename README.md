# Python Autoclicker

A simple CLI-based autoclicker tool built in Python using `pyautogui`.
It supports configurable delay, fixed/infinite clicking, saved settings, and a stop key.

---

## 🚀 Features

* Adjustable click delay (in seconds)
* Infinite or fixed click modes
* Live click counter with status display
* Save and load previous settings (JSON)
* Press **`q` anytime to stop the autoclicker**
* Simple command-line interface

---

## 📦 Requirements

* Python 3.x
* pyautogui
* keyboard

### Install dependencies:

```bash
pip install pyautogui keyboard
```

---

## ▶️ How to Run

```bash
python autoclicker.py
```

---

## ⚙️ How It Works

1. Enter delay between clicks
2. Choose click mode:

   * `inf` → infinite clicks
   * number → fixed number of clicks
3. Choose whether to reuse saved settings
4. Confirm start
5. Autoclicker begins after a short delay

---

## ⛔ Stop Feature

* Press **`q`** anytime during execution to stop the autoclicker safely

---

## 💾 Settings

The program saves your settings in:

```
settings.json
```

This includes:

* wait time
* total clicks

---

## 📌 Example Output

```
Click - 1 | Delay - 1 second(s) | Mode - Infinite
Click - 2 | Delay - 1 second(s) | Mode - Infinite
```

---

## ⚠️ Warning

This tool controls your mouse automatically.
Use carefully and avoid running it on important tasks.

---

## 🔮 Future Improvements

* GUI version (Tkinter)
* Hotkey start/stop toggle
* Better settings menu system
