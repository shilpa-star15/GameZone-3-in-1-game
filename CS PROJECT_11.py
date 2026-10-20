import tkinter as tk
import random as r
print("GAME ZONE\n")
end=0
while True:
    def r_s():
        global ww,ll,bn,i
        ww.destroy()
        print("ROLL AND SCORE")
        print("""
Rules

->Each player has to roll the dice.
->There are 20 positions to land on.
->When a person's total is 20,the game of that player is done!
->But here's the plot twist, at each position your points could
  increase/decrease or becomes null.Or nothing happens to your points.
->In the end when the game's over the total points will be calculated.
->The player with most points wins!
GOOD LUCK!!""")
                

        s=[]
        sc=[]
        f=[]
        l=[20,19,18,17,16,15,14]
        i=0
        def play():
            global ll
            global bn
            global n
            def roll():
                global i
                def dice():
                    if a==1:
                        print(""" _______
|       |
|       | 
|   ●   |
|       |
|_______|""")
                    elif a==2:
                        print(""" _______
|       |
| ●     | 
|       |
|     ● |
|_______|""")
                    elif a==3:
                        print(""" _______
|       |
| ●     | 
|   ●   |
|     ● |
|_______|""")
                    elif a==4:
                        print(""" _______
|       |
| ●   ● | 
|       |
| ●   ● |
|_______|""")
                    elif a==5:
                        print(""" _______
|       |
| ●   ● | 
|   ●   |
| ●   ● |
|_______|""")
                    elif a==6:
                        print(""" _______
|       |
| ●   ● | 
| ●   ● |
| ●   ● |
|_______|""")

                def fs():
                    if s[i] in [3,9,15]:
                        print("Player",i+1, "lost", s[i]//2, "point(s)")
                        sc[i]-=sc[i]//2
                    if s[i] in [4,8,12,16]:
                        print("Player",i+1,"gained", s[i]//2, "point(s)")
                        sc[i]+=s[i]//2
                    if s[i] in [5,10]:
                        print("Player",i+1,"lost all points")
                        sc[i]=0
                
                
                if f.count(20)==n:
                    ww.destroy()        
                if f[i]==0:
                    if s[i] not in l:
                        a=r.randint(1,6)
                        dice()
                        print("Player",i+1,"rolled:",a)
                        s[i]+=a
                        print("Player",i+1,"landed on",s[i])
                        fs()

                        
                        i+=1
                    else:
                        a=r.randint(1,6)
                        dice()
                        print("Player",i+1,"rolled:",a)
                        if a<=l.index(s[i]):
                            s[i]+=a
                            print("Player",i+1,"landed on:",s[i])
                            fs()
                            if s[i]==20:
                                print("PLAYER",i+1,"REACHED 20!!!")
                                f[i]=20
                        else:
                            print("Move not possible")
                        i+=1
                
                
                
                if i==n:
                    i=0
                while f[i]==20 and f.count(20)!=n:
                    i+=1
                    if i==n:
                        i=0
                if i in range(0,n) and f[i]==0:
                    print("Player",i+1,"roll the dice")
            n=int(en.get())
            for i in range(n):
                s.append(0)
                sc.append(0)
                f.append(0)
            ll.destroy()
            en.destroy()
            bn.destroy()
            print("Player 1 roll the dice")
            ww.rowconfigure([0,1,2],weight=1)
            ww.columnconfigure(0,weight=1)
            ll=tk.Label(master=ww,text="Press the button to roll the dice!!",height=2,width=30,\
                    font=("Fixedsys",15),bg="#10ffde")
            ll.grid(row=0,column=0,sticky="nsew")
            ll=tk.Label(master=ww,text="(Kindly don't close this window.\nOtherwise the game will end!)",\
                        height=2,width=50,font=("Fixedsys",7),bg="#10ffde")
            ll.grid(row=1,column=0,sticky="nsew")
            bn=tk.Button(master=ww,text="Roll",command=roll,bg="#dd33ff",activebackground="#770586",\
                          height=1,font=("Fixedsys",15))
            bn.grid(row=2,column=0,sticky="nsew")
            ww.mainloop()

        ww=tk.Tk()
        ww.title("ROLL AND SCORE")
        ww.rowconfigure([0,1,2],weight=1,minsize=35)
        ww.columnconfigure(0,weight=1)
        ll=tk.Label(master=ww,text="Enter number of players(2 or more)",bg="#a1ff6c",height=2,width=20,\
                    font=("Fixedsys",15))
        ll.grid(row=0,column=0,sticky="nsew")
        en=tk.Entry(master=ww,width=35,font=("Fixedsys",15))
        en.grid(row=1,column=0,sticky="nsew")
        bn=tk.Button(master=ww,text="Play",command=play,bg="#ff6c6c",activebackground="#db3333",\
                     height=1,font=("Fixedsys",15))
        bn.grid(row=2,column=0,sticky="nsew")
        ww.mainloop()

        print("SCORES:")
        m_n=max(sc)
        for i in range(n):
             print("Player",i+1,":",sc[i])
        if sc.count(sc[0])==n:
             print("DRAW!!")
        else:
             for i in range(len(sc)):
                  if sc[i]==m_n:
                       print("PLAYER",(i+1),"WINS!!")



    def rps():
            global ww,rnd,yp,cp
            ww.destroy()
            l=["Rock","Paper","Scissor"]
            d={"Rock":3,"Paper":1,"Scissor":2}
            rnd=1
            print("ROCK PAPER SCISSOR")
            print("""
Rules

->You play with computer.
->Each starts with 5 points
->You and computer play rounds of rock-paper-scissors.
->When one of the player loses all his points the game ends.
->The other one wins(more than 0 pts).
->Otherwise, if the game exceeds 20 rounds,the game ends.
->Players risk points during each round to use a move.
  Rock:3 points
  Paper:1 point
  Scissors: 2 points
->Players can only risk points such that their remaining points after a move is non-negative
  (i.e. player points ≥ 0).
->After a round is played, the winning player keeps their points risked
  and gains the points risked by the losing player.
->The losing player loses their points risked.
->If both players choose the same move, no points are lost/gained.
            """)
            print("ROUND 1")
            global main,func
            def main():
                
                global yp,cp,a,rnd
                
                rnd+=1
                print("You played",b)
                yp-=d[b]
                c=r.choice(l)
                while cp<d[c]:
                    c=r.choice(l)
                print("Computer played",c)
                cp-=d[c]
                if (b=="Rock" and c=="Scissor") or (b=="Paper" and c=="Rock") or (b=="Scissor" and c=="Paper"):
                    print("YOU WON THIS ROUND!!")
                    yp+=d[b]+d[c]
                    print("Your score:",yp)
                    print("Computer's score:",cp)
                elif b==c:
                    print("DRAW!!")
                    yp+=d[b]
                    cp+=d[c]
                    print("Your score:",yp)
                    print("Computer's score:",cp)
                else:
                    print("COMPUTER WON THIS ROUND!!")
                    cp+=d[b]+d[c]
                    print("Your score:",yp)
                    print("Computer's score:",cp)
                print()
            def func():
                global b
                b=l[a-1]
                if yp<d[b]:
                    print("You don't have enough points to play",b)
                else:
                    main()
                    if yp==0 or cp==0:
                        ww.destroy()
                    elif rnd>20:
                        ww.destroy()
                    else:
                        print("ROUND",rnd)
                
            def rock():
               global a
               a=1
               func()
            def paper():
               global a
               a=2
               func()
            def scissors():
               global a
               a=3
               func()
               

            yp=5
            cp=5
            ww=tk.Tk()
            ww.title("ROCK PAPER SCISSORS")
            ww.rowconfigure([0,1,2,3,4],weight=1)
            ww.columnconfigure(0,weight=1)
            ll=tk.Label(master=ww,text="Select your choice",font=("OCR A Extended",15),\
                        height=2,width=30,bg="#ff96ef")
            ll.grid(row=0,column=0,sticky="nsew")
            lll=tk.Label(master=ww,text="(Kindly don't close this window.\nOtherwise the game will end!)",\
                         font=("OCR A Extended",12),height=3,width=30,bg="#ff96ef")
            lll.grid(row=1,column=0,sticky="nsew")
            bn1=tk.Button(master=ww,text="Rock(3 pts)",command=rock,bg="#15a6f3",\
                          font=("OCR A Extended",12),height=2)
            bn2=tk.Button(master=ww,text="Paper(1 pt)",command=paper,bg="#53d71d",\
                          font=("OCR A Extended",12),height=2)
            bn3=tk.Button(master=ww,text="Scissors(2 pts)",command=scissors,bg="#f3553f",\
                          font=("OCR A Extended",12),height=2)
            bn1.grid(row=2,column=0,sticky="nsew")
            bn2.grid(row=3,column=0,sticky="nsew")
            bn3.grid(row=4,column=0,sticky="nsew")
            ww.mainloop()

            print("GAME OVER!!")
            print("SCORES:")
            print("YOUR SCORE:",yp)
            print("COMPUTER SCORE:",cp)
            if yp>cp:
                print("YOU WIN!!!")
            elif yp==cp:
                print("DRAW!!")
            else:
                print("COMPUTER WINS!!!")

    def tt():
            ww.destroy()
            print("TIC TAC TOE")
            def multi():
                global b
                print("Player 1, Enter",l,":",end='')
                b=int(input())
                if b not in l:
                    b=int(input("Spot occupied!!Pls enter(1-9):"))
                
            def comp():
                global b
                b=r.choice(l)
                print("Computer plays")
                
                
                
                        
            print("Multiplayer or Play with Computer?")
            print("1.Multiplayer")
            print("2.Play with computer")
            o=int(input("Enter 1 or 2:"))
            while o not in [1,2]:
                    o=int(input("Invalid input.Enter 1 or 2:"))
            print("TIC TAC TOE")
            print("  "+"1"+"  |  "+"2"+"  |  "+"3")
            print("-----|-----|-----")
            print("  "+"4"+"  |  "+"5"+"  |  "+"6")
            print("-----|-----|-----")
            print("  "+"7"+"  |  "+"8"+"  |  "+"9")
            p2=""
            d={1:" ",2:" ",3:" ",4:" ",5:" ",6:" ",7:" ",8:" ",9:" "}
            l=[1,2,3,4,5,6,7,8,9]
            print("Player 1 is X")
            print("Player 2 is O")
            def box():
                print("  "+d[1]+"  |  "+d[2]+"  |  "+d[3])
                print("-----|-----|-----")
                print("  "+d[4]+"  |  "+d[5]+"  |  "+d[6])
                print("-----|-----|-----")
                print("  "+d[7]+"  |  "+d[8]+"  |  "+d[9])
            box()
            while True:
                print("Player 1, Enter",l,":",end='')
                a=int(input())
                if a not in l:
                    print("Spot occupied!!Please enter",l,":",end='')
                    a=int(input())
                if a in l:
                    d[a]="X"
                    l.remove(a)
                    box()
                    if d[1]==d[2]==d[3]=="X" or d[4]==d[5]==d[6]=="X" or d[7]==d[8]==d[9]=="X" or d[1]==d[5]==d[9]=="X" or d[3]==d[5]==d[7]=="X" or d[1]==d[4]==d[7]=="X" or d[2]==d[5]==d[8]=="X" or d[3]==d[6]==d[9]=="X":
                        print("PLAYER 1 WINS!!")
                        break
                if len(l)==0:
                    print("Draw")
                    break
                if o==1:
                    multi()
                    p2="PLAYER 2"
                if o==2:
                    comp()
                    p2="COMPUTER"
                
                if b in l:
                    d[b]="O"
                    l.remove(b)
                    box()
                    if d[1]==d[2]==d[3]=="O" or d[4]==d[5]==d[6]=="O" or d[7]==d[8]==d[9]=="O" or d[1]==d[5]==d[9]=="O" or d[3]==d[5]==d[7]=="O" or d[1]==d[4]==d[7]=="O" or d[2]==d[5]==d[8]=="O" or d[3]==d[6]==d[9]=="O":
                        print(p2,"WINS!!")
                        break
                if len(l)==0:
                    print("DRAW")
                    break
    def exi():
        ww.destroy()
        global end
        end=1
    if end==1:
        print("Thanks for visiting! Come back again!")
        break


    ww=tk.Tk()
    ww.rowconfigure([0,1,2,3,4,5],weight=1,minsize=45)
    ww.columnconfigure(0,weight=1)
    ww.title("GAME")
    ll=tk.Label(master=ww,text="GAME ZONE",bg="#ff6b21",height=4,font=("Consolas",23,"bold"),width=30)
    ll.grid(row=0,column=0,sticky="nsew")
    ll=tk.Label(master=ww,text="Welcome!!\nWhat do you want to play?\nClick the button below",\
                bg="#cdff11",height=4,\
                font=("Consolas",12),width=30)
    ll.grid(row=1,column=0,sticky="nsew")
    bn1=tk.Button(master=ww,text="Roll and Score(Multiplayer Dice Game)",command=r_s,bg="#a244f0",\
                  font=("Consolas",12),width=30)
    bn2=tk.Button(master=ww,text="Rock Paper Scissors",command=rps,bg="#ff4bf4",\
                  font=("Consolas",12),width=30)
    bn3=tk.Button(master=ww,text="Tic Tac Toe",command=tt,bg="#28c4ff",\
                  font=("Consolas",12),width=30)
    bn4=tk.Button(master=ww,text="Exit",command=exi,bg="#43a715",\
                  font=("Consolas",12),width=30)
    bn1.grid(row=2,column=0,sticky="nsew")
    bn2.grid(row=3,column=0,sticky="nsew")
    bn3.grid(row=4,column=0,sticky="nsew")
    bn4.grid(row=5,column=0,sticky="nsew")
    ww.mainloop()
