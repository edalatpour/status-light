import time
import urllib.request
import json
from unicornhatmini import UnicornHATMini

uh = UnicornHATMini()

def get_user_status(email):
    api_url = 'https://jrubeasp5d.execute-api.us-east-1.amazonaws.com/'
    request = api_url + email

    response = urllib.request.urlopen(request)
    #html = response.read().decode('utf-8')

    data = json.load(response)

    return data['userStatus']

def color(r, g, b):
    for x in range(17):
        for y in range(7):
            uh.set_pixel(x, y, r, g, b)
    uh.show()

def clear():
    uh.clear()
    uh.show()

def startup():
    uh.set_brightness(0.25)
    sleep = 0.25
    clear()
    color(255, 0, 0)
    time.sleep(sleep)
    color(255, 255, 0)
    time.sleep(sleep)
    color(0, 255, 0)
    time.sleep(sleep)
    color(0, 255, 255)
    time.sleep(sleep)
    color(0, 0, 255)
    time.sleep(sleep)
    color(255, 0, 255)
    time.sleep(sleep)
    clear()

# startup()
uh.set_brightness(0.5)
email = 'edalatpour@hotmail.com'

last_status = ''

while True:

    try:
        status = get_user_status(email)
        status = status.strip().lower()
        if status != last_status:
            if status == 'red':
                print('red')
                color(255, 0, 0)
            if status == 'green':
                print('green')
                color(0, 255, 0)
            last_status = status
    finally:
        time.sleep(1)
