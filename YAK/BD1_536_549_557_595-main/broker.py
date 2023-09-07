import socket
import os

HOST = "127.0.0.1"  
PORT = 65432  

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
            ans=data.decode()
            x=ans.split(".")
            
            try:
                directory = x[0]
                parent_dir = "C:/Users/HP/Desktop/BIG DATA project/B1"
                path = os.path.join(parent_dir, directory)
                os.mkdir(path)
                f = open("C:/Users/HP/Desktop/BIG DATA project/B1/{}/{}.txt".format(x[0],x[0]), "x")
                f.write("\n{}".format(x[1]))
                f.close()

                directory2 = x[0]
                parent_dir2 = "C:/Users/HP/Desktop/BIG DATA project/B2"
                path2 = os.path.join(parent_dir2, directory2)
                os.mkdir(path2)
                f2 = open("C:/Users/HP/Desktop/BIG DATA project/B2/{}/{}.txt".format(x[0],x[0]), "x")
                f2.write("\n{}".format(x[1]))
                f2.close()

                directory3 = x[0]
                parent_dir3 = "C:/Users/HP/Desktop/BIG DATA project/B3"
                path3 = os.path.join(parent_dir3, directory3)
                os.mkdir(path3)
                f3 = open("C:/Users/HP/Desktop/BIG DATA project/B3/{}/{}.txt".format(x[0],x[0]), "x")
                f3.write("\n{}".format(x[1]))
                f3.close()
            except:
                f = open("C:/Users/HP/Desktop/BIG DATA project/B1/{}/{}.txt".format(x[0],x[0]), "a")
                f.write("\n{}".format(x[1]))
                f.close()
                

                f2 = open("C:/Users/HP/Desktop/BIG DATA project/B2/{}/{}.txt".format(x[0],x[0]), "a")
                f2.write("\n{}".format(x[1]))
                f2.close()
            

                f3 = open("C:/Users/HP/Desktop/BIG DATA project/B3/{}/{}.txt".format(x[0],x[0]), "a")
                f3.write("\n{}".format(x[1]))
                f3.close()















       