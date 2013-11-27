import hashlib
import random
import string
import os
hashes = 0
found = 0

def mine():
    global hashes, found
    found = 0
    while True:
        starter = ''.join([random.choice(
            string.uppercase + string.lowercase + string.digits)
            for x in range(5)])
        on = 0
        while True:
            c = hashlib.sha512(str(on) + starter).hexdigest()
            startswith = "1" * 7
            if c.startswith(startswith):
                found += 1
                x = file("coins.txt", "r")
                data = x.read()
                x.close()
                x = file("coins.txt", "w")
                x.write(data + "\n" + str(on) + starter)
                x.close()
                break
            else:
                on += 1
            hashes += 1
from time import sleep
from threading import Timer

def hello():
    global hashes, found
    t = Timer(2.0, hello)
    t.start()
    os.system('cls' if os.name=='nt' else 'clear')
    print str(hashes/2000) + "KH/S"
    print 'Coins Found: ' + str(found)
    hashes = 0
t = Timer(2.0, hello)
t.start()
mine()
