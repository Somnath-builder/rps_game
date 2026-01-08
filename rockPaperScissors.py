'''
r:rock=1
p:paper=0
s:scissors=-1
'''
import random  #generates random number
from datetime import datetime
import winsound  #makes beep sound
from playsound import playsound
mainDict={"r":1,"p":0,"s":-1}
chDict={1:"rock", 0:"paper",-1:"scissors"}
def game(computer,human):
    diff=computer-human
    if (diff==0):
        print("IT'S A DRAW 🥲")
        return 0
    elif ((diff==1) or (diff==-2)):
        playsound("win.mp3")
        print("CONGRATS, YOU WON !!😎")
        return 1
    elif ((diff==-1) or (diff==2)):
        playsound("lose.mp3")
        print("OOPS,YOU LOST !!😶‍🌫")
        return -1
win=lose=draw=total=0
player=input("\nPlease enter your name:").upper()
print(f"WELCOME {player}\nlet's play rock-paper-scissors")
while True:        
    choice=input(" enter \n r for rock\n p for paper\n s for scissors\n q to quit\n:").lower()
    winsound.Beep(1000, 200)   #(frequency,time in ms)
    if(choice=="q"):
        print("farewell 👋🏻")
        break
    if choice not in mainDict:
        print("invalid choice")
    else:    
        computer=random.choice([1,0,-1])
        human=mainDict[choice]
        compCh=chDict[computer]
        humCh=chDict[human]
        print(f"computer's choice:{compCh}\n your choice:{humCh}")
        score=game(computer,human)
        if score==1:
            win+=1  
        elif score==-1:
            lose+=1  
        else:
            draw+=1 
        total+=1       
        print(f"SCORE:\n YOU:{win}\t COMPUTER:{lose}\tDRAW:{draw}\tTOTAL:{total}")
        rate=(win*100)/total
        print(f"win-rate={rate}") 
if total!=0:
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")        
    with open("rpsScores.txt","a") as f:
        f.write(f"\n {player}:{win}\tCOMPUTER:{lose}\tDRAW:{draw}\tTOTAL:{total}\t{time}")


        
            
        


