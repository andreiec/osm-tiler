from selenium import webdriver
import folium
import time
import os
from pynput.keyboard import Key, Controller

htmlFile = 'map.html'
keyboard = Controller()

foliumMap = folium.Map(
    tiles='https://api.mapbox.com/styles/v1/andreiec/cl2c2f5g5000p14mzejpm2gml/tiles/256/{z}/{x}/{y}@2x?access_token=pk.eyJ1IjoiYW5kcmVpZWMiLCJhIjoiY2o4Nzd2M2g5MTJjZDMzbzA1bnFtYnJuYyJ9.Y6xX5guQFCUhjFvjNuPrgQ',
    zoom_start=17,
    max_zoom=17,
    attr='Mapbox Attribution',
    location=[36.3182, 139.4332]
)

foliumMap.save(htmlFile)

browser = webdriver.Firefox(executable_path="C:/Users/andre/Desktop/geckodriver.exe")
tmpurl = 'file://{path}/{mapfile}'.format(path=os.getcwd(), mapfile=htmlFile)

foliumMap.save(htmlFile)
browser.get(tmpurl)

# Walk on map
moveToRight = True

for i in range(1, 2501):

    # Wait to load
    time.sleep(1)

    # If 200 steps to right, move down and change direction to left
    if i % 50 == 0:
        moveToRight = not moveToRight

        for j in range(7):
            keyboard.press(Key.down)
            time.sleep(0.1)
            keyboard.release(Key.down)
            time.sleep(0.2)

    # Save screenshot
    browser.save_screenshot("files/images/" + str(i) + ".png")

    # Move to next position
    for j in range(7):
        keyboard.press(Key.right if moveToRight else Key.left)
        time.sleep(0.1)
        keyboard.release(Key.right if moveToRight else Key.left)
        time.sleep(0.2)

    print(f"Image number: {i}")
