"""
python >=3.7

pip install joycon-python
pip install hidapi
pip install pyautogui
"""
import numpy as np
import time
from pyjoycon import device
from pyjoycon.joycon import JoyCon

import pyautogui

component = np.array([0.82522979, 0.29479633, 0.48175815])
thres_zero = 500
thres_upper = 2000
coef = 0.0002

unit_meter = 10
target = unit_meter

print("Finding JoyCon-L...")
ids = device.get_ids("L")
joycon = JoyCon(*ids)
print("    Done.")

print("Wait for 5 seconds...")
time.sleep(5)

cumscore = 0
acc_old = np.array([joycon.get_accel_x(), joycon.get_accel_y(), joycon.get_accel_z()])

print("    Done.")
print("Started!")
while 1:
    time.sleep(0.02)
    acc = np.array([joycon.get_accel_x(), joycon.get_accel_y(), joycon.get_accel_z()])
    delta = acc - acc_old
    acc_old = acc

    score = np.abs(np.dot(delta, component))
    if score < thres_zero:
        score = 0
    score = min(score, thres_upper)
    score *= coef

    cumscore += score
    if target < cumscore:
        pyautogui.press("up")
        target += unit_meter

    print("\r                                     ", end="")
    print("\r score: {:d}\ttotal score: {:d}".format(int(score), int(cumscore)), end="")
