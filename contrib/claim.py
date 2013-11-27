import socket
import hashlib
import json
import random
import string
import sqlite3
import threading
import time

def check_coin(data):
    node = sqlite3.connect("nodes.db")
    node = node.execute("SELECT ip, port FROM data WHERE relay=?", [True]) 
    node = node.fetchall()
    random.shuffle(node)
    for x in node:
        s = socket.socket()
        try:
            s.settimeout(1)
            s.connect((x[0], x[1]))
        except:
            s.close()
            continue
        else:
            data['cmd'] = "check_coin"
            s.send(json.dumps(data))
        s.close()
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
        return i + 1

print 'Loading Coin Sender...'
total = file_len('coins.txt')
i = 1
with open('coins.txt') as f:
    print "Submitting coins. This could take a bit."
    for line in f:
      time.sleep(1)
      line = line[:-1]
      c = hashlib.sha512(line).hexdigest()
      wall = sqlite3.connect("wallet.db")
      address = wall.execute("SELECT address FROM data")
      address = address.fetchall()[0][0]
      check_coin({"starter":line, "hash":c, "address":address})
      print 'Coin Added: [' + line + '] Number: ' + str(i) + ' of ' + str(total)
      i +=1