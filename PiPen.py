#PiPen
from sense_hat import sense_hat
import requests

colour = 0
colours = [[255, 0, 0], [255, 255, 0], [0, 255, 0], [0, 255, 255], [0, 0, 255], [128, 0, 255], [255, 0, 191], [255,255,255]]
coloursHex = ["#ff0000","#ffff00", "#00ff00", "#00ffff", "#0000ff", "#8000ff", "#ff00bf", "#000000" ]
# Colours: Red, Yellow, Green, Light Blue, Dark blue, pink, purple, black


sense = SenseHat()

def send(data):
	r = requests.post('http://localhost:8080', data)


for i in range(0, len(colours) - 1):
	sense.set_pixel(i, 3, colours[i])


while True:
    x, y = sense.get_accelerometer_raw().values()

    x=round(x, 0)
    y=round(y, 0)

    print("x=%s, y=%s" % (x, y))
    send({"x":x, "y":y, "colour": coloursHex[colour]})


  send({"x":1, "y":2, "colour": coloursHex[colour]})