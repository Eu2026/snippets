import random
import os
import gettext

while True:
    language_choice = raw_input("Chose your language (ro/en) ")
    if language_choice.lower() == 'ro' or language_choice.lower() == 'en':
        break
language = gettext.translation('fazan', localedir='locale', languages=[language_choice])
language.install()


class Player(object):
    """
    Manage the usere's actions and his score

    Attributes:
        attr1 (str): stores the player name
        attr2 (bool): stores the last round result
        attr3 (str): stores the answer
        attr4 (str): the key word to end the game
        attr5 (int): counts the lost rounds
    Methods:
        my_turn
        add_faz
    """
    def __init__(self, name, win_turn=True, answer="", fazan="", score=1):

        self.name = name
        self.fazan = fazan
        self.answer = answer
        self.win_turn = win_turn
        self.score = score

    def my_turn(self):
        """Get the answer from keyboard and return it"""

        self.answer = raw_input(_("raspunsul tau: "))
        return self.answer

    def add_faz(self):
        """Updates the key word based on lost rounds"""
        if self.score == 1:
            self.fazan = self.fazan + 'f'

        elif self.score == 2:
            self.fazan = self.fazan + 'a'

        elif self.score == 3:
            self.fazan = self.fazan + 'z'

        elif self.score == 4:
            self.fazan = self.fazan + 'a'

        elif self.score == 5:
            self.fazan = self.fazan + 'n'
        self.score += 1


class Computer(Player):
    """
    Inherits the Player class and manage the computer's actions and his score

    Attributes:
        Same as inherited class, but the __init__ function calls the
        Player's __init__ with "Computer" as first parameter

    Methods:
        my_turn -- override the superclass method;
    """

    def __init__(self):
        super(Computer, self).__init__(_("Calculator"))

    def my_turn(self, pref):
        """Get a random word from word_list and return it"""

        global word_list
        random_word = random.choice(word_list[pref])
        word_list[pref].remove(random_word)
        return random_word

files_in_dir = os.listdir('.')  # a list containing the names of the entries in the current directory
word_list = {}  # a dictionary containing the words categorized by their prefixes
for file in files_in_dir:
    if '.txt' in file:
        key = file.rstrip('.txt')
        g = open(file, "r")
        word_list[key] = [line.rstrip('\n') for line in g]


def player_turn(pref, player):
    """Check if there is a word with the given prefix
        and return False or the usere's answer.

        Args:
            attr1 (str): the given prefix
            attr2 (Player): the player whoes turn is
    """
    if pref in word_list:
        print _("Prefixul pentru cuvantul tau este: "), pref
        i = 0
        while i < 3:
            choice = player.my_turn()
            if choice in word_list[pref]:
                word_list[pref].remove(choice)
                break
            i += 1
        else:
            print _("Ai esuat in a gasi un cuvant, ai fost inchs! ")
            return False
        print _("Cuvant acceptat! ")
        return choice
    else:
        print _("Nu exista cuvant cu acest prefix, ai fost inchis!")
        return False


def computer_turn(pref, computer):
    """Return False or an word with the given prefix.

        Args:
            arg1 (str): the given prefix
            arg2 (Computer): the object whoes turn is
    """

    if pref in word_list:
        choice = computer.my_turn(pref)
        return choice
    print _("Felicitari, m-ai inchis! ")
    return False

computer = Computer()
name = raw_input(_("numele tau: "))
player = Player(name)

while(player.fazan != 'fazan' and computer.fazan != 'fazan'):

    random_key = random.choice(word_list.keys())
    current_word = random.choice(word_list[random_key])
    while True:
        print _('Cuvantul curent:'), current_word
        current_word = player_turn(current_word[len(current_word)-2:len(current_word)], player)  # -2 since there is no '\n' i have to send just the last 2 characters
        if current_word is not False:
                current_word = computer_turn(current_word[len(current_word)-2:len(current_word)], computer)  # same thing as abobe, sending just 2 characters
                if current_word is False:
                    computer.add_faz()
                    break
                else:
                    print _("Raspunsul calculatorului: "), current_word
        else:
            player.add_faz()
            break

    print player.name + ':', player.fazan
    print computer.name + ':', computer.fazan
