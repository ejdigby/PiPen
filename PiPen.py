#PiPen
# from sense_hat import sense_hat

import requests


# sense = SenseHat()

def send(data):
	r = requests.post('http://localhost:8080', data)

send({'key':'value'})