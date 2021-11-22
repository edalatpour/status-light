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

color_map = {'red': (255,0,0),
             'orange': (255,140,0),
             'yellow': (255,255,0),
             'green': (0,205,0),
             'blue': (0,0,255),
             'purple': (128,0,128)}

while True:

    try:
        status = get_user_status(email)
        status = status.strip().lower()
        if status != last_status:
#            if status == 'red':
#                print('red')
#                color(255, 0, 0)
#            if status == 'green':
#                print('green')
#                color(0, 255, 0)
            (r,g,b) = color_map[status]
            color(r,g,b)
            last_status = status

    except:
        print('error')
    finally:
        time.sleep(10)
