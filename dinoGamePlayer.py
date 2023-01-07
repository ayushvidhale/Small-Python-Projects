import pyautogui as p 
import time as t 
print('PLAYING') 
t.sleep(5) 
p.press('space') 
def avoid_obstacles(): 
    x = p.pixelMatchesColor(545,223,(83,83,83)) 
    if x : 
        p.press('space') 
while True: 
    avoid_obstacles() 