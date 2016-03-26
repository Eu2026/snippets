import random
import os
class Player(object):
    def __init__(self,nume,win_turn= True, raspuns= "",fazan="",scor=1):
        self.nume = nume
        self.fazan = fazan
        self.raspuns = raspuns
        self.win_turn = win_turn
        self.scor = scor
    def my_turn(self):
        self.raspuns = raw_input("Raspunsul tau: ")
        return self.raspuns
    def add_faz(self):
        if self.scor == 1:
            self.fazan = self.fazan + 'f'

        elif self.scor == 2:
            self.fazan = self.fazan + 'a'

        elif self.scor == 3:
            self.fazan = self.fazan +'z'

        elif self.scor == 4:
            self.fazan = self.fazan +'a'

        elif self.scor == 5:
            self.fazan = self.fazan +'n'
        self.scor += 1


class Calculator(Player):
     def __init__(self):
         super(Calculator,self).__init__("Calculator")
     def my_turn(self,pref):
        f = open(pref + '.txt','r+')
        s = 0
        lines = []
        for line in f:
            lines.append(line)
        f.seek(0)
        rand = random.randrange(len(lines))
        cuv = lines[rand]
        del lines[rand]
        for line in lines:
            f.write(line)
        f.close()
        return cuv

def player_turn(pref,player):
    pref = pref.replace('\n',"")
    try:
        f  = open(pref + '.txt','r+')
    except IOError:
        print "Ai fost incuiat, nu exista niciun cuvant care incepe cu", pref
        return False
    lines = []
    f.seek(0)
    for line in f:
        lines.append(line)


    print "Prefixul pentru cuvantul tau este: ", pref
    i = 0

    while i < 3:
        alegere = player.my_turn();
        alegere = alegere + '\n'


        if alegere in lines:
            lines.remove(alegere)
            f.seek(0)
            for line in lines:
                f.write(line)
            break;
        i += 1

    else:
        print "Ai esuat in a gasi un cuvant, ai fost inchis! "
        f.close()
        return False
    print "Cuvant acceptat! "
    f.close()
    return alegere

def computer_turn(pref,computer):
    pref = pref.replace('\n',"")
    try:
        f  = open(pref + '.txt','r+')
    except IOError:
        print "Felicitari, ai inchis calculatorul! ", pref
        return False

    alegere = computer.my_turn(pref)
    return alegere


computer = Calculator()
nume = raw_input("Numele tau: ")
player = Player(nume)

while(player.fazan != 'fazan' and computer.fazan != 'fazan'):
    s = random.randrange(0,300)
    k = 0
    files_in_dir = os.listdir('.')
    for file_in_dir in files_in_dir:
        k = k+1
        if k == s:
            g = open(file_in_dir,'r+')
    s = 0
    lines = []
    for line in g:
        lines.append(line)
    g.seek(0)
    rand = random.randrange(len(lines))
    cuv_curent = lines[rand]
    del lines[rand]
    for line in lines:
        g.write(line)

    while True:
           print 'Cuvantul curetnt:',cuv_curent
           cuv_curent = player_turn(cuv_curent[len(cuv_curent)-3:len(cuv_curent)],player)
           if cuv_curent != False:
                   cuv_curent = computer_turn(cuv_curent[len(cuv_curent)-3:len(cuv_curent)],computer)
                   if cuv_curent == False:
                       computer.add_faz()
                       break
                   else:
                       print "Raspunsul calculatorului: ", cuv_curent
           else:
               player.add_faz();
               break

    print player.nume + ':', player.fazan
    print computer.nume + ':', computer.fazan
