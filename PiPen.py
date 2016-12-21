#PiPen - Pi Code
from sense_hat import SenseHat
import requests

#Setup Colours
# Colours: Red, Yellow, Green, Light Blue, Dark blue, pink, purple, black
colour = 0
colours = [[255, 0, 0], [255, 255, 0], [0, 255, 0], [0, 255, 255], [0, 0, 255], [128, 0, 255], [255, 0, 191], [255,255,255]]
coloursHex = ["#ff0000","#ffff00", "#00ff00", "#00ffff", "#0000ff", "#8000ff", "#ff00bf", "#000000" ]

#Initialize pygame and sense
sense = SenseHat()

#Define Send Function
def send(data):
	r = requests.post('http://localhost:8080', data)


#Draw colours on matrix
for i in range(0, len(colours) - 1):
	sense.set_pixel(i, 3, colours[i])


while True:
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    x=round(x, 0)
    y=round(y, 0)
    z=round(z, 0)

    print("x={0}, y={1}, z={2}".format(x, y, z))
  
    print("x=%s, y=%s, color=%s" % (x, y, coloursHex[colour]))
    #Send latest data
    send({"x":x, "y":y, "colour": coloursHex[colour]})

