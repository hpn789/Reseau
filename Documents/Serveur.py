import socket
import select
import time

class Joueur:

    num = 0

    def __init__(self):
        self.num = Joueur.num
        Joueur.num+=1
        self.nbBourses=0
        self.nbDiamants=0
        self.nbBalles=0
        self.pioche = []
        self.main = []
        self.position=0

    def reinit(self):
        self.nbBourses=0
        self.nbDiamant=0
        self.nbBalles=0
        self.pioche = []
        self.main = []
        self.position=0

class Wagon:

    def __init__(self,nb1, nb2):
        nbBourses = nb1
        nbDiamants = nb2

class Game:

    def __init__(self):
        self.tourJoueur = 0
        self.pileCarte = []
        self.numManche = 0
        self.numTour=0
        self.positionMarshall=0
        self.positionValise=0

hote = ''
port = 1337

tcpConnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpConnection.bind((hote, port))
tcpConnection.listen(4)
print("Server on port {}".format(port))

serverOn = True
connectedClients = []

lastTick = time.time()
elapse = 1.0
nbTick = 0

while serverOn:

    newConnections, wlist, xlist = select.select([tcpConnection], [], [], 0.05)

    for c in newConnections:
        connection, info = c.accept()
        connectedClients.append(connection)

    clientToRead = []
    try:
        clientToRead, wlist,xlist = select.select(connectedClients, [], [], 0.05)
    except select.error:
        pass
    else:
        for client in clientToRead:
            msg = client.recv(1024)
            msg = msg.decode()
            print("Reçu {}".format(msg))
            if msg == "fin":
                serverOn = False
        if time.time()-lastTick>=elapse:
            lastTick = time.time()
            nbTick+=1
            if nbTick>9:
                serverOn = False
            for client in connectedClients:
                client.send(b"Tick")
            
        
        

print("Close connections")
for c in connectedClients:
    c.send(b"fin")
    c.close()

tcpConnection.close();
