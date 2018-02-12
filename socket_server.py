import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 8001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

print 'Server start at: %s:%s' %(HOST, PORT)
print 'wait for connection...'

while True:
    conn, addr = s.accept()
    print 'Connected by ', addr
    
    # Use 'while True:' loop to receive data to avoid overbuffer data loss
    while True:
        data = conn.recv(1024)
        if data == ':q': break
    
        conn.send("server received you message.")
# conn.close()
