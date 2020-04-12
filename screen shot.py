import pyautogui
import time
for i in range(6):
  x = pyautogui.screenshot()
  x.save("{}.png".format(i))
  time.sleep(3)


