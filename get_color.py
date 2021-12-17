import logging
import time
import urllib.request
import json
from gpiozero import Button
from unicornhatmini import UnicornHATMini

# Set up logging
log = "/home/pi/status-light/out.log"
logging.basicConfig(filename=log,level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

uh = UnicornHATMini()

def get_user_status(email):
    api_url = 'https://jrubeasp5d.execute-api.us-east-1.amazonaws.com/'
    request = api_url + email
    #logging.info(request)
    #print(request)
    response = urllib.request.urlopen(request)
    html = response.read().decode('utf-8')

    #data = json.load(response)

    #return data['userStatus']
    return html

def set_user_status(email, color_name):
    api_url = 'https://jrubeasp5d.execute-api.us-east-1.amazonaws.com/'
    request = api_url + email + '/' + color_name
    #logging.info(request)
    #print(request)
    response = urllib.request.urlopen(request)
    status_code = response.read().decode('utf-8')
    return status_code

def show_rgb(r, g, b):
    for x in range(17):
        for y in range(7):
            uh.set_pixel(x, y, r, g, b)
    uh.show()
    
def show_color(color_name):
    (r,g,b) = color_map[status]
    show_rgb(r,g,b)

def clear():
    uh.clear()
    uh.show()

def pressed(button):
    color_name = ''
    if button == button_a:
        color_name = 'green'
    if button == button_b:
        color_name = 'red'
    if button == button_x:
        color_name = 'blue'
    if button == button_y:
        color_name = 'black'
    status = set_user_status(email, color_name)
    show_color(color_name)
    color_name = get_user_status(email)
    show_color(color_name)

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
             'green': (0,205,0),
             'blue': (0,0,255),
             'black': (0,0,0)}

button_a = Button(5)
button_b = Button(6)
button_x = Button(16)
button_y = Button(24)

try:
    button_a.when_pressed = pressed
    button_b.when_pressed = pressed
    button_x.when_pressed = pressed
    button_y.when_pressed = pressed
except KeyboardInterrupt:
    button_a.close()
    button_b.close()
    button_x.close()
    button_y.close()

while True:

    try:
        status = get_user_status(email)
        status = status.strip().lower()
        if status != last_status:
            logging.info(status)
            print(status)
        show_color(status)

    except Exception as ex:
        logging.info(ex)
        print(ex)
        clear()

    finally:
        last_status = status
        time.sleep(5)
