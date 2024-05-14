from serial import Serial
from time import sleep, time

serial_port = '/dev/cu.usbmodemF412FA6F2F702'

connection = Serial(serial_port, 115200)

while (True):

    message = 'TBoop\n'


    print(message, time())

    connection.write(message.encode('utf-8'))
    sleep(0.9)
    # while connection.in_waiting < 0:
    #     print("waiting for message")

    # response = connection.readline()
    # print(response)

