import socket

HOST = "127.0.0.1"  
PORT = 65432  

topics=[]


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        topic=input("Enter topic :")
        topics.append(topic)
        message=input("Enter the message :")
        res = bytes(topic+'.'+message, 'utf-8')
        s.sendall(res)
        data = s.recv(1024)

print(f"Received {data!r}")