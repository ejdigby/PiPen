#PiPen - Pi Code                                                                                                                                          
from sense_hat import SenseHat
import requests
from evdev import InputDevice, list_devices, ecodes
import sys
from asyncore import file_dispatcher, loop



class InputDeviceDispatcher(file_dispatcher):

    def __init__(self, device):
        self.device = device
        file_dispatcher.__init__(self, device)
    def recv(self, ign=None):
        return self.device.read()
    def handle_read(self):
        for event in self.recv():
            print(repr(event))
#Setup Colours                                                                                                                                            
# Colours: Red, Yellow, Green, Light Blue, Dark blue, pink, purple, black                                                                                 
colour = 0
colours = [[255, 0, 0], [255, 255, 0], [0, 255, 0], [0, 255, 255], [0, 0, 255], [128, 0, 255], [255, 0, 191], [255,255,255]]
coloursHex = ["#ff0000","#ffff00", "#00ff00", "#00ffff", "#0000ff", "#8000ff", "#ff00bf", "#000000" ]

#Initialize pygame and sense                                                                                                                              
sense = SenseHat()
sense.clear()

#Define Send Function                                                                                                                                     
def send(data):
    r = requests.post('http://localhost:8080', data)


#Draw colours on matrix                                                                                                                                   
for i in range(0, len(colours) - 1):
    sense.set_pixel(i, 3, colours[i])
found = False;
devices = [InputDevice(fn) for fn in list_devices()]
for dev in devices:
    if dev.name == 'Raspberry Pi Sense HAT Joystick':
        found = True;
    break
if not(found):
    print('Raspberry Pi Sense HAT Joystick not found. Aborting ...')
    exit()

def handle_code(code):
    if code == ecodes.KEY_LEFT and colour > 0:
        colour -= 1 
        print("Left")
    elif code == ecodes.KEY_RIGHT and colour < 7:
        print("Right")
        colour += 1
while True:
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    x=round(x, 0)
    y=round(y, 0)
    z=round(z, 0)
#       print("x={0}, y={1}, z={2}".format(x, y, z))                                                                                                      

    print("x=%s, y=%s, color=%s" % (x, y, coloursHex[colour]))
    #Send latest data                                                                                                                                 
    send({"x":x, "y":y, "colour": coloursHex[colour]})
    InputDeviceDispatcher(dev)

  
# >>> dev = InputDevice('/dev/input/event1')



# InputDeviceDispatcher(dev)
# loop()