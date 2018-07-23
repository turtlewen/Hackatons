import random
import string
import datetime

#random generate letter
def letterGenerator():
    boogle =[]
    for x in range(0,16):
        letter=random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        boogle.append(letter)
    print(" -----------------")
    print (" | "+boogle[0]+" | "+boogle[1]+" | "+boogle[2]+" | "+boogle[3]+" | ")
    print (" | "+boogle[4]+" | "+boogle[5]+" | "+boogle[6]+" | "+boogle[7]+" | ")
    print (" | "+boogle[8]+" | "+boogle[9]+" | "+boogle[10]+" | "+boogle[11]+" | ")
    print (" | "+boogle[12]+" | "+boogle[13]+" | "+boogle[14]+" | "+boogle[15]+" | ")
    print(" -----------------")

def checkWord(ansList):
    f = open("words_alpha.txt")

    for a in ansList:

        if len(a.lower()) <=2:
            continue
        else:
            for b in f:
                if b == a.lower():
                    print(b)
    

letterGenerator()


after3min = datetime.datetime.now() + datetime.timedelta(minutes = 3)


ans=''
ansList=[]

while ans!="0":
    ans = raw_input("Enter your answer: ")
    ansList.append(ans)

    if datetime.datetime.now() == after3min:
        print("time is over")
        break
    
    
checkWord(ansList)

       
