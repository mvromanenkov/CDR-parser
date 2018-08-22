# script requirements:
#   - python 3 (tested on 3.6.5)
#       -- pysocket
#       -- pymssql

import socket
import pymssql

### Initial constants ###

# TCP connection setup
HOST = ''
PORT = 1234
ADDR = (HOST,PORT)
BUFSIZE = 4096

# DATABASE setup
DBADDR = 'dbaddr'
DBNAME = 'dbname'
DBUSER = 'dbuser'
DBPASS = 'dbpass'

DBCRED = {'server':DBADDR,'database':DBNAME,'user':DBUSER,'password':DBPASS}

DBTBL = 'AVAYACDR'
DBFLD = '([date],[time],[vdn],[calling-num],[dialed-num],[sec-dur],[in-trk-code],[clg-num-in-tac],[in-crt-id],[out-crt-id],[duration],[code-used])'

### END Initial constants ###

# Connecting DataBase

try:
    conn = pymssql.connect(**DBCRED)
    query = conn.cursor()
except:
    print('Error while connecting DB.')

# Starting port listener
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(ADDR)
serv.listen(5)

# Start accepting data 
while True:
    c, addr = serv.accept()
    while True:
        data = c.recv(BUFSIZE)
        if not(b'\x00\x00\x00' in data):
            #received data is 'binary', converting to strings:
            str = data.decode("utf-8")
            #splitting text to fixed length fields (see 'change system-parameter cdr' on GEDI):
            item=(str[0:6],str[7:11],str[12:16],str[18:33],str[35:50],str[52:57],str[59:63],str[65:80],str[82:85],str[87:90],str[92:96],str[98:102])
            #preparing SQL query:
            query.execute("INSERT INTO "+DBTBL+" "+DBFLD+" VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');" % (item))
            #executing it:
            conn.commit()
