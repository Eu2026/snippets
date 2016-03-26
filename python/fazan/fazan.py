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
        global word_list
        cuv = random.choice(word_list[pref])
        word_list[pref].remove(cuv)
        return cuv



files_in_dir = os.listdir('.')
word_list  = {}
for file in files_in_dir:
 
    if '.txt' in file:
        key = file.rstrip('.txt')
        g = open(file,"r")
        word_list[key] = [line.rstrip('\n') for line in g]
        
        


def player_turn(pref,player):
    if pref in word_list:
        print "Prefixul pentru cuvantul tau este: ", pref
        i = 0
        while i < 3:
            alegere = player.my_turn();
 
            if alegere in word_list[pref]:
                word_list[pref].remove(alegere)
                break
            i += 1           
        else:
            print "Ai esuat in a gasi un cuvant, ai fost inchs! "
            return False
        print "Cuvant acceptat! "
        return alegere
    else:
        print "Nu exista cuvant cu acest prefix, ai fost inchis!"
        return False
 
def computer_turn(pref,computer):
    pref = pref.replace('\n',"")
    if pref in word_list:
        alegere = computer.my_turn(pref)
        return alegere
    print "Felicitari, m-ai inchis! "
    return False

computer = Calculator()
nume = raw_input("Numele tau: ")
player = Player(nume)

while(player.fazan != 'fazan' and computer.fazan != 'fazan'):
     
     rand1 = random.choice(word_list.keys())
     cuv_curent = random.choice(word_list[rand1])
     
       
       
     while True:
           print 'Cuvantul curent:',cuv_curent
           cuv_curent = player_turn(cuv_curent[len(cuv_curent)-2:len(cuv_curent)],player)
           if cuv_curent != False:
                   cuv_curent = computer_turn(cuv_curent[len(cuv_curent)-2:len(cuv_curent)],computer)
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
