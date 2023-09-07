import socket
import os

HOST = "127.0.0.1"  
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        topic=input("Enter the Topic to read: ")
        try:
            f = open("C:/Users/HP/Desktop/BIG DATA project/B1/{}/{}.txt".format(topic,topic), "r")
            print(f.read())
            f.close()

            '''f = open("C:/Users/HP/Desktop/BIG DATA project/B2/{}/{}.txt".format(topic,topic), "r")
            print(f.read())
            f.close()

            f = open("C:/Users/HP/Desktop/BIG DATA project/B3/{}/{}.txt".format(topic,topic), "r")
            print(f.read())
            f.close()'''
        except:
            parent_dir = "C:/Users/HP/Desktop/BIG DATA project/B1"
            path = os.path.join(parent_dir,topic)
            os.mkdir(path)

            parent_dir2 = "C:/Users/HP/Desktop/BIG DATA project/B2"
            path2 = os.path.join(parent_dir2,topic)
            os.mkdir(path2)

            parent_dir3 = "C:/Users/HP/Desktop/BIG DATA project/B3"
            path3 = os.path.join(parent_dir3,topic)
            os.mkdir(path3)
