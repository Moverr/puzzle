from flask import Flask,render_template
import random
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ROWS = 12
COLS = 12
wordsearch = []


# todo: this is going to supply the index page, which is going to bascially 
@app.route('/')
def index():
    wordsearch = []
    words = ["A"]
    for row in range(0,ROWS):
        wordsearch.append([])
        for col in range(0,COLS):
            wordsearch[row].append("-")
        
    for row in range(0,ROWS):
        for col in range(0,COLS):            
            randomLetter = random.choice(LETTERS)
            print(randomLetter)
            wordsearch[row][col]=randomLetter
    
    # return  str(wordsearch)
    askmoie(wordsearch)
    addWord(words,wordsearch)
    return render_template("index.html",wordsearch=wordsearch)

    
def askmoie(wordsearch):
    print(" " + ("_"*COLS*2) + "_ ")
    print("|" + (" "*COLS*2) + " |")
    for row in range(0,ROWS):
        line="| "
        for col in range(0,COLS):
            line = line + wordsearch[row][col] + " "
            line = line + "|"
            print(line)
    print("|" + ("_"*COLS*2) + "_|")  

def addWord(word,wordsearch):
    placed=False
    attempts = 0
    while not placed and attempts<100: #Avoid infinite loops if the program can't find a place for a word.
        attempts +=1
        direction = random.randint(0,5)
    #Decide Starting Row and Col Position for the first letter of the wor
    #Decide horizontal step (hs) and vertical step (vs)
    
        if len(word)>ROWS or len(word)>COLS:
            print("Some of your words are too long for this grid. Remove long words or resize your grid.")
            # exit()
    
        if direction==0: #Horizontal Left to Right
            row=random.randint(0,ROWS - 1)
            col=random.randint(0,COLS - len(word))
            hs=1
            vs=0
        elif direction==1: #Vertical Top - To Bottom
            row=random.randint(0,ROWS - len(word))
            col=random.randint(0,COLS - 1) 
            hs=0
            vs=1      
        elif direction==2: #Diagonal Top Left - To Bottom Right
            row=random.randint(0,ROWS - len(word))
            col=random.randint(0,COLS - len(word))  
            hs=1
            vs=1      
        if direction==3: #Horizontal Right to Left
            row=random.randint(0,ROWS - 1)
            col=random.randint(len(word)-1,COLS - 1)
            hs=-1
            vs=0
        elif direction==4: #Vertical Top - To Bottom
            row=random.randint(len(word)-1,ROWS - 1)
            col=random.randint(0,COLS - 1) 
            hs=0
            vs=-1      
        elif direction==5: #Diagonal Top Left - To Bottom Right
            row=random.randint(len(word)-1,ROWS - 1)
            col=random.randint(len(word)-1,COLS - 1)  
            hs=-1
            vs=-1      

    #Check if words fit without colliding with other letters
        collision=False
        for i in range(0,len(word)):
            if (wordsearch[row+vs*i][col+hs*i]!="-" and wordsearch[row+vs*i][col+hs*i]!=word[i]):
                collision=True
    #Collision means we can addthe word to the gird
        if not collision:
            for i in range(0,len(word)):
                wordsearch[row+vs*i][col+hs*i]=word[i]
                placed=True

        if not placed:
            print("Program aborted. Try again, remove words from your list or increase the size of the grid.")
            # exit()







if __name__ == '__main__':
    app.run(debug=True)
