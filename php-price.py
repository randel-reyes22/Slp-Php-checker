import requests
import json
import os
import time
import pywintypes
from win10toast import ToastNotifier

toast = ToastNotifier()
toast.show_toast("SLP Price Check", "The checker has been started", duration = 5)

os.chdir("C:\Slp-Php-checker")

while True:
    #http address or api address for the request
    coin = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=smooth-love-potion&vs_currencies=php").text
    coin = json.loads(coin)
    #float for to display decimal points
    price = (float(coin["smooth-love-potion"]["php"]))
    #message to the system tray
    os.system(f"notify-send -t 50000 \"Smooth Love Potion\" \"The price of SLP is {price}\"")
    #sleep for 1 minute
    time.sleep(60)