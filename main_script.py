# import package
import time
import pyautogui

# set var
click_counter = 0
wait_time = 0
total_clicks = 0

# click function
def click(delay, mode):
    global click_counter # state global var
    click_counter += 1 # increase var count
    print(f"Click - {click_counter} | Delay - {delay} second(s) | Mode - {mode}")
    pyautogui.click() # click

print("--Welcome to Autoclicker--")
time.sleep(0.1)
while True:
    try:
        wait_time = int(input("Enter delay of autoclicker (whole number): ").strip())
    except ValueError:
        print("Invalid input, retry.")
        continue

    print("\nEnter loop count \n'inf' - Infinite clicks\n0+ - Fixed clicks")
    raw_total_clicks = input().strip()
    if raw_total_clicks == "inf":
        total_clicks = 0
    else:
        try:
            total_clicks = int(raw_total_clicks)
        except ValueError:
            print("Please enter valid input, a positive number/'inf'")   
            continue
    break

print("Start autoclicker? (y/n)")
yes_no  = input().strip()
if yes_no in ['y', 'yes']:
    print("Autoclicker will start in 3 seconds")
    time.sleep(3)
    print("\nAutoclicker started.")

    # loop
    if total_clicks == 0:
        autoclick_mode = "Infinite"
        while True:
            click(wait_time, autoclick_mode) # call function
            time.sleep(wait_time) # wait
    else:
        autoclick_mode = "Fixed"
        for i in range(total_clicks):
            click(wait_time, autoclick_mode) # call function
            time.sleep(wait_time) # wait

elif yes_no in ['n', 'no']:
    print("Autoclicker has been cancelled.")

print("Exit.")