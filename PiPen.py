#PiPen - Pi Code
import os

os.environ["SDL_VIDEODRIVER"] = "dummy"

#Import Libraries
from sense_hat import sense_hat
import requests
import pygame

#Setup Colours
# Colours: Red, Yellow, Green, Light Blue, Dark blue, pink, purple, black
colour = 0
colours = [[255, 0, 0], [255, 255, 0], [0, 255, 0], [0, 255, 255], [0, 0, 255], [128, 0, 255], [255, 0, 191], [255,255,255]]
coloursHex = ["#ff0000","#ffff00", "#00ff00", "#00ffff", "#0000ff", "#8000ff", "#ff00bf", "#000000" ]

#Initialize pygame and sense
pygame.init()
pygame.display.set_mode((640, 480))
sense = SenseHat()

#Define Send Function
def send(data):
	r = requests.post('http://localhost:8080', data)


#Draw colours on matrix
for i in range(0, len(colours) - 1):
	sense.set_pixel(i, 3, colours[i])

while True:
	#Get Accelerometer Data
    x, y = sense.get_accelerometer_raw().values()

    x=round(x, 0)
    y=round(y, 0) 

    for event in pygame.event.get():	
    	if event.type == KEYDOWN:
    		#When pushed right, change colour to the right by 1
            if event.key == K_RIGHT and colour < 7:
                colour += 1
            #When pushed left, change colour to the right by 1
            elif event.key == K_LEFT and colour > 0:
            	colour -= 1

  
    print("x=%s, y=%s, color=%s" % (x, y, coloursHex[colour]))
    #Send latest data
    send({"x":x, "y":y, "colour": coloursHex[colour]})

