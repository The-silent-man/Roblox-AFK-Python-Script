import keyboard as key
import time

def afk():
    # Ensures the Script Runs forever until stopped by user
    while True:
        # 20 minutes of waiting till execution of script
        time.sleep(1200)
        key.press('a')
        time.sleep(0.5)
        key.release('a')
        key.press('d')
        time.sleep(0.5)
        key.release('d')

print("""Starting script. Make sure you tab back into roblox.
You can always stop the script early by pressing CTRL+C in the console/terminal""")

afk()
