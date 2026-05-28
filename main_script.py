# import package
import time
import pyautogui
import json
import os
import keyboard

# set var
click_counter = 0
wait_time = 0
total_clicks = 0
saved_settings = {}
cancelled = False

# click function
def click(delay, mode):
    global click_counter # state global var
    click_counter += 1 # increase var count
    print(f"Click - {click_counter} | Delay - {delay} second(s) | Mode - {mode}")
    pyautogui.click() # click

def save_settings(settings):
    with open("settings.json", "w") as f:
        json.dump(settings, f)

def load_settings():
    with open("settings.json", "r")as f:
        try:
            return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
    
def get_settings():
    # clicker settings
    while True:
        try:
            w_time = int(input("Enter delay of autoclicker (whole number): ").strip())
        except ValueError:
            print("Invalid input, retry.")
            continue

        print("\nEnter loop count \n'inf' - Infinite clicks\n0+ - Fixed clicks")
        raw_total_clicks = input().strip()
        if raw_total_clicks == "inf":
            tot_click = 0
        else:
            try:
                tot_click = int(raw_total_clicks)
            except ValueError:
                print("Please enter valid input, a positive number/'inf'")   
                continue
        return w_time, tot_click

print("--Welcome to Autoclicker--")
time.sleep(0.1)

while True:
    if os.path.exists("settings.json"):
        print("Would you like to use past settings? (y/n)")
        settings_yes_no = input().strip().lower()

        if settings_yes_no in {'y', 'yes'}:
            saved_settings = load_settings()
            wait_time = saved_settings["wait_time"]
            total_clicks = saved_settings["total_clicks"]
            break

        elif settings_yes_no in {'n', 'no'}:
            wait_time, total_clicks = get_settings()
            saved_settings = {"wait_time": wait_time, "total_clicks": total_clicks}
            save_settings(saved_settings)
            break
        else:
            print("Invalid option, retry")
            continue
    else:
        wait_time, total_clicks = get_settings()
        saved_settings = {"wait_time": wait_time, "total_clicks": total_clicks}
        save_settings(saved_settings)
        break
        

print("Start autoclicker? (y/n)")
start_yes_no  = input().strip().lower()
# main loop
if start_yes_no in ['y', 'yes']:
    print("Autoclicker will start in 3 seconds")
    print("Press 'q' anytime to cancel autoclicker")
    time.sleep(3)
    print("\nAutoclicker started.")

    # loop
    if total_clicks == 0:
        autoclick_mode = "Infinite"
        while True:
            click(wait_time, autoclick_mode)
            for _ in range(wait_time * 10):
                if keyboard.is_pressed('q'):
                    cancelled = True
                    break
                time.sleep(0.1)
            if cancelled:
                break 
    else:
        autoclick_mode = "Fixed"
        for i in range(total_clicks):
            click(wait_time, autoclick_mode) # call function
            for _ in range(wait_time * 10):
                
                if keyboard.is_pressed('q'):
                    cancelled = True
                    break
                time.sleep(0.1) 
            if cancelled:
                break 

elif start_yes_no in ['n', 'no']:
    print("Autoclicker has been cancelled.")

print("\nExit.")
