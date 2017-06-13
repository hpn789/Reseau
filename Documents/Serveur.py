import socket
import select
import time

class CardType():
    ESCAPE=0
    CLIMB=1
    GUN=2
    ROBERY=3
    SHERIFF=4
    PUNCH=5
    BALL=6

class Joueur:

    num = 0

    def __init__(self):
        self.num = Joueur.num
        Joueur.num+=1
        self.nbBourses=1
        self.nbDiamants=0
        self.nbBalles=0
        self.pioche = []
        self.main = []
        self.position=2

    def reinit(self):
        self.nbBourses=0
        self.nbDiamant=0
        self.nbBalles=0
        self.pioche = []
        self.main = []
        self.position=0

class Emplacement:

    def __init__(self,nb1, nb2):
        self.nbBourses = nb1
        self.nbDiamants = nb2

class Game:

    def __init__(self):
        self.tourJoueur = 0
        self.pileCarte = []
        self.numManche = 0
        self.numTour=0
        self.positionMarshall=0
        self.positionValise=0
        self.state = 0

class Carte:

    def __init__(self, num):
        self.visible=True
        self.ID=num

def identifieCardType(num):
    if num>63 and num<77:
        return CardType.CARD
    num%=16
    if num<=0 and num<6:
        return CardType.BALL
    if num<=6 and num<8:
        return CardType.ESCAPE
    if num<=8 and num<10:
        return CardType.CLIMB
    if num<=10 and num<12:
        return CardType.GUN
    if num<=12 and num<14:
        return CardType.ROBERY
    if num==14:
        return CardType.SHERIFF
    if num==15:
        return CardType.PUNCH
    return -1


def sendGameState():
    numJoueur=0
    infosJoueurs=[]
    mainJoueurs = []
    infosTrain = ""
    autresInfos = ""

    
    for j in joueurs:
        infos=str(j.nbBalles)+sep2+str(j.position)+sep2+str(j.nbBourses)+sep2+str(j.nbDiamants)
        main=""
        for c in j.main:
            main+=str(c.ID)+sep2
        if len(j.main)>0:
            main = main[:-1]
            
        infosJoueurs.append(infos)
        mainJoueurs.append(main)
        

    for emp in train:
        infosTrain+=""+str(emp.nbBourses)+sep2+str(emp.nbDiamants)+sep3
        
    if len(train)>0:
        infosTrain = infosTrain[:-1]

    autresInfos = str(game.positionValise)+sep1+str(game.positionMarshall)+sep1
    if len(game.pileCarte)>0:
        autresInfos+=str(game.pileCarte[-1].ID)+sep2
        if game.pileCarte[-1].visible:
            autresInfos+="1"
        else:
            autresInfos+="0"
    else:
        autresInfos+="0"+sep2+"-1"
    
    for client in connectedClients:
        msg = str(game.tourJoueur)+sep1
        for infos in infosJoueurs:
            msg+=infos+sep1
        msg+=mainJoueurs[numJoueur]+sep1
        msg+=infosTrain+sep1+autresInfos+sep1+str(game.state)+"\n"
        client.send(str.encode(msg))
        
        numJoueur+=1

def initGame():
    
    for i in range(0, 10):
        train.append(Emplacement(0,i))

    for i in range(0, 4):
        j=Joueur()
        for k in range(44,52):
            j.main.append(Carte(k))
        joueurs.append(j)

    for i in range(0,5):
        game.pileCarte.append(Carte(i))

def action(numJoueur, idCarte, numAction):
    print("action")
    

hote = ''
port = 1337

sep1 = "|"
sep2 = "~"
sep3 = " "

tcpConnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpConnection.bind((hote, port))
tcpConnection.listen(4)
print("Server on port {}".format(port))

serverOn = True
connectedClients = []

lastTick = time.time()
elapse = 1.0
nbTick = 0

game = Game()
train = []
joueurs = []

initGame()

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
            if nbTick>100:
                serverOn = False
            sendGameState()
            
        
        

print("Close connections")
for c in connectedClients:
    c.send(b"fin")
    c.close()

tcpConnection.close();
    
