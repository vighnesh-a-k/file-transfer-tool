
import socket
import tqdm
import os
import server
import client

SERVER_HOST = 'localhost'
SERVER_PORT = 5001
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

CLIENT_HOST = 'localhost'
CLIENT_PORT = 5001

if __name__ =="__main__":

    #setting up
    if str(input("press 0 for send 1 to recieve"))=="1":
        server_instance=server.Server(SERVER_HOST,SERVER_PORT,socket.AF_INET, socket.SOCK_STREAM)
        print("server waiting")
        try:
            server_instance.bind()
    
        except socket.error as message:
            print('Bind failed. Error Code ')
        
        server_instance.listen()

        client_socket, address = server_instance.accept()
        received = client_socket.recv(BUFFER_SIZE).decode()

        filename, filesize = received.split(SEPARATOR)
        filename = os.path.basename(filename)
        filesize = int(filesize)

        with open("recieve"+filename) as f:
            while True:
                bytes_read = server_instance.recv(BUFFER_SIZE)
                if not bytes_read:
                    break
                f.write(bytes_read)
        server_instance.close()















    
    
    else:
       
        
        
        
        
        
        
        client_instance=client.Client(CLIENT_HOST,CLIENT_PORT,socket.AF_INET, socket.SOCK_STREAM)
        print("client waiting")
        try:
            client_instance.connect((CLIENT_HOST,CLIENT_PORT))
            print("connected succesfully")
        except socket.error as message:
            print('connect failed. Error Code : '
                + str(message[0]) + ' Message '
                + message[1])

        filename = input("photo.jpeg")
        filesize = os.path.getsize(filename)
        client_instance.send(f"{filename}{SEPARATOR}{filesize}".encode())
        with open(filename, "rb") as f:
            while True:
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:
                    break
                client_instance.sendall(bytes_read)
        client_instance.close()
        
        
