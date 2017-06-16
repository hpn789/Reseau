import socket
import select
import time
import random

class CardType():
    ESCAPE=0
    CLIMB=1
    GUN=2
    ROBERY=3
    SHERIFF=4
    PUNCH=5
    BALL=6

class State():
    WAIT=0
    PLAY=1
    SHOW=2
    QUESTION=3
    END=4
    WIN=4
    LOOSE=5

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
        self.score=0
        self.name=""

    def reinit(self):
        self.nbBourses=0
        self.nbDiamant=0
        self.nbBalles=0
        self.pioche = []
        self.main = []
        self.position=0
        self.score=0

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
        self.state = State.WAIT
        self.descriptif=""
        self.nbBalles = 0

class Carte:

    def __init__(self, num):
        self.visible=True
        self.ID=num

def identifieCardType(num):
    if num>63 and num<77:
        return CardType.BALL
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

def addCard(card):
    game.pileCarte.append(Carte(card))


def sendGameState(isBegin, isEnd):
    numJoueur=0
    infosJoueurs=[]
    mainJoueurs = []
    infosTrain = ""
    autresInfos = ""
    score = ""

    if isEnd:
        for j in joueurs:
            score+=str(j.score)+sep3
        score=score[:-1]
    
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
        msg+=infosTrain+sep1+autresInfos+sep1+str(game.state)

        if isBegin:
            if numJoueur==0:
                msg+=sep1+"0"+sep3+"1"+sep3+"2"+sep3+"3"
            elif numJoueur==1:
                msg+=sep1+"1"+sep3+"2"+sep3+"3"+sep3+"0"
            elif numJoueur==2:
                msg+=sep1+"2"+sep3+"3"+sep3+"0"+sep3+"1"
            elif numJoueur==2:
                msg+=sep1+"3"+sep3+"0"+sep3+"1"+sep3+"2"
        elif isEnd:
            msg+=sep1+score
            
        
        msg+=+"\n"
        client.send(str.encode(msg))
        
        numJoueur+=1

def initGame():
    
    for i in range(0, 10):
        bourses = 0
        diamants =0
        if i==1:
            bourses=3
        elif i==2:
            bourses=4
            dimants=1
        elif i==3:
            bourses=3
            diamants=1
        elif i==4:
            bourses=1
        train.append(Emplacement(bourses,diamants))

    game.nbBalles = 13

    names = ["Belle", "Doc", "Cheyenne", "Ghost"]
    for i in range(0, 4):
        j=Joueur()
        for k in range(i*16+6, (i+1)*16):
            j.pioche.append(Carte(k))
        j.name = names[i]
        joueurs.append(j)

    game.pileCarte=[]

def playCard(card):
    needAnswer = False
    idCard = card.ID
    numJoueur = game.tourJoueur
    descriptif = ""

    typeCard = identifieCardType(idCard)
    if CardType.GUN:
        #action a completer
        listJoueurs = []
        if joueurs[numJoueur].position>4:
            for i in range(0, len(joueurs)):
                if joueurs[i].position>4:
                    listJoueurs.append(i)
            if len(listJoueurs)==0:
                descriptif = joueurs[numJoueur].name+" tire mais personne n'est là"
            else:
                indiceJoueurToucher = listJoueurs[random.randint(0, len(listJoueurs-1))]
                if joueurs[numJoueur].nbBalles==0:
                    descriptif = j.name+" tire mais n'a plus de balles"
                else:
                    joueurs[numJoueur].nbBalles-=1
                    joueurs[indiceJoueurToucher].pioche.append(Carte(numJoueur*16+joueurs[numJoueur].nbBalles))
                    descriptif = j.name+" tire et touche "+joueurs[indiceJoueurToucher].name
        else:
            for i in range(0, len(joueurs)):
                if joueurs[i].position<4 and joueurs[i].position!=joueurs[numJoueur].position and (joueurs[i].position+1==joueurs[numJoueur].position or joueurs[i].position-1==joueurs[numJoueur].position) :
                    listJoueurs.append(i)

            if len(listJoueurs)==0:
                descriptif = joueurs[numJoueur].name+" tire mais personne n'est là"
            else:
                indiceJoueurToucher = listJoueurs[random.randint(0, len(listJoueurs-1))]
                if joueurs[numJoueur].nbBalles==0:
                    descriptif = joueurs[numJoueur].name+" tire mais n'a plus de balles"
                else:
                    joueurs[numJoueur].nbBalles-=1
                    joueurs[indiceJoueurToucher].pioche.append(Carte(numJoueur*16+joueurs[numJoueur].nbBalles))
                    descriptif = joueurs[numJoueur].name+" tire et touche "+joueurs[indiceJoueurToucher].name
            
            
    if CardType.ESCAPE:
        #action a completer
        needAnswer=True
        descriptif=j.name+" bouge"
    if CardType.CLIMB:
        #action a completer
        if j.position>4:
            j.position-=5
            descriptif=j.name+" descend"
        else:
            j.position+=5
            descriptif=j.name+" monte"
        
    if CardType.BALL:
        #action a completer
        descriptif=j.name+" ne fait rien"
    if CardType.ROBERY:
        #action a completer
        if game.positionValise==joueurs[numJoueur].position:
            game.positionValise = len(train)-1+numJoueur
            descriptif=joueurs[numJoueur].name+" pille la valise"
        if train[joueurs[numJoueur].position].nbDiamants>0:
            train[joueurs[numJoueur].position].nbDiamants-=1
            joueurs[numJoueur].nbDiamants+=1
            descriptif=joueurs[numJoueur].name+" pille un diamant"
        elif train[joueurs[numJoueur].position].nbBourses>0:
            train[joueurs[numJoueur].position].nbBourses-=1
            j.nbBourses+=1
            descriptif=joueurs[numJoueur].name+" pille une bourse"
        else:
            descriptif=joueurs[numJoueur].name+" pille mais le wagon est vide"
    if CardType.SHERIFF:
        #action a completer
        needAnswer=True
        descriptif=joueurs[numJoueur].name+" bouge le Sheriff"
    if CardType.PUNCH:
        #action a completer
        listJoueurs = []
        
        for i in range(0, len(joueurs)):
            if joueurs[i].position==joueurs[numJoueur].position:
                listJoueurs.append(i)

        if len(listJoueurs)==0:
            descriptif = joueurs[numJoueur].name+" punch mais personne n'est là"
        else:
            indiceJoueurToucher = listJoueurs[random.randint(0, len(listJoueurs-1))]
            move = random.randint(0,1)
            descriptif = joueurs[numJoueur].name+" punch "+joueurs[indiceJoueurToucher].name
            if game.positionValise-9 == indiceJoueurToucher:
                game.positionValise = joueurs[numJoueur].position
                descriptif+=" qui perd la valise"
            elif joueurs[indiceJoueurToucher].nbDiamants>0:
                joueurs[indiceJoueurToucher].nbDiamants-=1
                train[joueurs[indiceJoueurToucher].position].nbDiamants+=1
                descriptif+=" qui perd un diamant"
            elif joueurs[indiceJoueurToucher].nbBourses>0:
                joueurs[indiceJoueurToucher].nbBourses-=1
                train[joueurs[indiceJoueurToucher].position].nbBourses+=1
                descriptif+=" qui perd une bourse"
            else:
                descriptif+=" qui ne perd rien"
                
            if joueurs[indiceJoueurToucher].position==4 or joueurs[indiceJoueurToucher]==9:
                    move=1
            if joueurs[indiceJoueurToucher].position==0 or joueurs[indiceJoueurToucher]==5:
                    move=0
                
            if move==0:
                joueurs[indiceJoueurToucher]+=1
                descriptif+=" et pars à droite"
            else:
                joueurs[indiceJoueurToucher]-=1
                descriptif+=" et pars à gauche"
        
    #resolution sheriff
    descriptif+=". "
    game.descriptif = descriptif
    return needAnswer;

def resolutionSheriff():
    for j in joueurs:
        if game.positionMarshall == j.position:
            j.position+=5
            if game.nbBalles>0:
                game.nbBalles-=1
                j.pioche.append(Carte(64+nbBalles))
    
def distribCards():
    for j in joueurs:
        j.main=[]
        j.pioche = melange(j.pioche)
        for i in range(0,9):
            j.main.append(j.pioche[i])

def echange(array, i, j):
    return array[:i] + array[j] + array[i+1:j] + array[i] + array[j+1:]

def melange(array, nb):
    for k in range(0,nb):
        for i in range(0, len(array)):
            for j in range(0, len(array)):
                array = echange(array, i, j)
    return array

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

nbJoueursMin = 1

while serverOn:

    newConnections, wlist, xlist = select.select([tcpConnection], [], [], 0.05)

    if game.state==State.WAIT:
        
        for c in newConnections:
            connection, info = c.accept()
            connectedClients.append(connection)

        if len(connectedClients)==nbJoueursMin:
            game.stat==PLAY
            distribCards()
            sendGameState(True, False)
            
    elif game.state==State.PLAY:
        
        clientToRead = []
        try:
            clientToRead, wlist,xlist = select.select(connectedClients, [], [], 0.05)
        except select.error:
            pass
        else:
            for client in clientToRead:
                if client == connectedClients[tourJoueur]:
                    msg = client.recv(1024)
                    msg = msg.decode()
                    parsedMsg = msg.split(sep3)
                    if len(parsedMsg)==2 and int(parsedMsg[0])==0:
                        addCard(int(parsedMsg[1]))
                        sendGameState(False, False)
                        game.tourJoueur+=1
                        game.numTour+=1
                        if numTour==5:
                            state=State.SHOW
                            game.pileCard.append(Card(81))
                            game.tourJoueur=0

    elif game.state==State.SHOW:
        game.pileCarte.remove(game.pileCarte[-1])
        card = game.pileCarte[-1]
        if playCard(card):
            state==State.QUESTION
        else:
            sendGameState(False, False)
            tourJoueur+=1

    elif game.QUESTION:
        for client in clientToRead:
                if client == connectedClients[tourJoueur]:
                    msg = client.recv(1024)
                    msg = msg.decode()
                    parsedMsg = msg.split(sep3)
                    if len(parsedMsg)==2 and int(parsedMsg[0])==2:
                        playMove(int(parsedMsg[1]), game.pileCarte[-1])
                        sendGameState(False, False)
                        game.tourJoueur+=1
                        state=State.SHOW

        
        

print("Close connections")
for c in connectedClients:
    c.send(b"fin")
    c.close()

tcpConnection.close();
    
