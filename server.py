import socket

class Server (socket.socket):
    def __init__(self,host,port,type1,type2):
        super().__init__(type1,type2)
        self.host=host
        self.port=port
    
    def info(self):
        print(f"working as {self.host}:{self.port}")
            
    def bind(self):
        super().bind((self.host,self.port))