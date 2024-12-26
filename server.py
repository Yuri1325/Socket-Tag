#Imports
import pickle
from _thread import *
import socket
from Constants import Constants
from Player import Player
import images
import pygame
from images import *

#Constants
Constants = Constants()

#Varibles & Lists
currentClient = 0

clientInfo = [Player(50,300),Player(750,300,False)]

#Making the socket
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.bind((Constants.SERVER,Constants.PORT))
socket.listen(2)
print("[SERVER STARTED] Waiting for connection...............")

def threadedClient(conn,client):
    global currentClient
    conn.send(pickle.dumps(clientInfo[client]))
    reply = ""
    data = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            clientInfo[client] = data
            if not data :
                print("[DISCONNECTING] ")
                break
            if (client==0):
                reply= clientInfo[1]
            else:
                reply = clientInfo[0]
        except:
            break
        conn.sendall(pickle.dumps(reply))

    print(f"[DISCONNECTING] Client {client} disconected")
    currentClient -=1
    conn.close()
while True:
    
    conn,addr = socket.accept()
    print(f"[NEW CONNECTION] Client {currentClient}",addr)
    start_new_thread(threadedClient,(conn,currentClient))
    currentClient+=1