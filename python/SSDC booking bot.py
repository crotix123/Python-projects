import pyautogui as pg
import pyscreenshot as ps
import time
import winsound
import telegram_send
time.sleep(5)
x = 0
while x <= 500:
    px1=ps.grab().load()
    colour1 = px1[836,1004]
    print(colour1)
    if colour1 != (202,21,66):
        pg.moveTo(1549,231,1)
        pg.click()
        pg.moveTo(1056,713,1)
        pg.click()
        pg.moveTo(609,391,1)
        pg.click()
        pg.moveTo(1531,480,1)
        pg.click()
        time.sleep(5)
        pg.scroll(-1000000000)
        pg.moveTo(301,464,1)
        pg.click()
        pg.moveTo(369,536,1)
        pg.click()
        time.sleep(2)
    else:
        pg.moveTo(836,1004,1)
        pg.click()
        time.sleep(2)
        px2=ps.grab().load()
        colour2 = px2[1145,263]
        print(colour2)
        if colour2 == (202,21,66):
            x += 0
            pg.moveTo(1145,263,2)
            pg.click()
            pg.press('f5')
            time.sleep(1)
        else:
            x += 600
        while x >= 600:
            winsound.Beep(440, 200)
            telegram_send.send(messages=["You have a practical slot!"])

