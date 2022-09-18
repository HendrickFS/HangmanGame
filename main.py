from getpass import getpass

def printHangman(lifes, secret,trieds):
    print("\n")
    print("\n")
    print("+-------------+")
    print("|             |    ",trieds)

    if lifes == 7:
        print("|             ")
    elif lifes < 7:
        print("|             O")
    elif lifes == 0:
        print("|             0")
    
    if lifes > 5:
        print("|             ")
    elif lifes > 4:
        print("|             |")
    elif lifes > 3:
        print("|            /|")
    elif lifes <= 3:
        print("|            /|\\")
    
    if lifes > 2:
        print("|             ")
    elif lifes > 1:
        print("|            / ")
    elif lifes > 0:
        print("|            / \\")
    
    print("|                     ",secret)
    print("+----------------------------")
    print("\n")

def printEnd(status):
    print("  +--------------------+")
    print("  |     GAME OVER      |")
    print("  +--------------------+")
    if status == 2:
        print("  +--------------------+")
        print("  |      YOU LOSE      |")
        print("  +--------------------+")
    elif status == 1:
        print("  +--------------------+")
        print("  |      YOU WIN       |")
        print("  +--------------------+")

#status: 0 = playing , 1 = win , 2 = lose
class forca:
    def __init__(self,lifes,word,letters,secretWord,status,points):
        self.lifes=lifes
        self.word=word
        self.letters=letters
        self.secretWord=secretWord
        self.status=status
        self.points=points
    
    def trie(self):
        printHangman(self.lifes,self.secretWord,self.letters)
        
        letter = input("(º_º)   Try some letter\n       -> ")
        while letter.upper() in self.letters:
            letter = input("(º_º)   Try OTHER letter\n       -> ")
        
        listSecret=list(self.secretWord)
        find=False
        
        for i in range(len(self.secretWord)):
            if letter.upper() == self.word[i]:
                listSecret[i]=letter.upper()
                self.secretWord="".join(listSecret)

                self.letters.append(letter.upper())
                self.points+=1
                
                find=True
        if not find:
                self.letters.append(letter.upper())        
                self.lifes-=1
        
        if self.lifes == 0:
            self.status = 2
            return True
        
        if self.points == len(self.word):
            self.status = 1
            return True
        
        return False

def start():
    typedWord=getpass("(¬_¬)   Type the word\n       -> ")
    confirmation=getpass("(¬_¬)   Confirm the word\n       -> ")
    
    while(typedWord!=confirmation):
        print("(*_*)   ERROR, DIFERENT WORDS!")
        typedWord=getpass("(¬_¬)   Type the word\n       -> ")
        confirmation=getpass("(¬_¬)   Confirm the word\n       -> ")
    
    secret=""
    for i in typedWord:
        secret+="_"
    word=typedWord.upper()
    letterList=[]
    game = forca(7,word,letterList,secret,0,0)
    
    return game

def main():
    game = start()
    gameover=False
    while not gameover:
        gameover=game.trie()
    printEnd(game.status)

main()