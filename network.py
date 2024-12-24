#Imports
from Constants import Constants
import socket
import pickle


#Constants
Constants = Constants()
#Making the class
class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.addr =(Constants.SERVER,Constants.PORT)
        self.startingPos = self.Connect()

    def Connect(self):
        self.client.connect(self.addr)
        return pickle.loads(self.client.recv(2048))
    def Send (self,objct):
       self.client.send(pickle.dumps(objct))
       return pickle.loads(self.client.recv(2048))

