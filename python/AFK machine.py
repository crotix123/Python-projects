import pyautogui as pg
import time
time.sleep(60)

try:
    while True:
        pg.moveTo(100, 200, 1)
        time.sleep(1)
        pg.moveTo(100, 1000, 1)
        time.sleep(1)
        pg.moveTo(1900, 1000, 1)
        time.sleep(1)
        pg.moveTo(1900, 200, 1)
        time.sleep(1)
except KeyboardInterrupt:
    exit()