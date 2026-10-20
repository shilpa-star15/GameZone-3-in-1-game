import tkinter as tk
import random as r
import threading
import time
import mysql.connector as sqltor
mycon=sqltor.connect(host='localhost',user='root',passwd='s1234',database='speed_game')
cursor=mycon.cursor()

def maths():
    global tim,scre
    def timer():
        global t,cl,tim
        t=60
        while True:
            try:
                lb["text"]=t
                win.update()
            
            
                t-=1
                
                if t<0:
                    time.sleep(0.5)
                    close()
                    break
                if cond==False:
                    break
                    
                
            except RuntimeError:
                pass
            
            tim+=1
            time.sleep(1)
            
    def close():
        win.destroy()
        print("Time taken:",tim)
        print("Score:",scre)
        cursor.execute("select * from maths_leaderboard")
        data=cursor.fetchall()
        names={}
        for i in data:
            names[i[0]]=(i[1],i[2])
            
        if uid in names:
            if names[uid][0]<scre or (names[uid][0]==scre and names[uid][1]>tim):
                comd="update maths_leaderboard set score={},time_taken_sec={} where userid='{}'".format(scre,tim,uid)
            else:
                comd=""
        elif uid=="" and scre==0 and tim==0:#i.e the user closes the enter username window
            comd=""

        else:
            comd="insert into maths_leaderboard(userid,score,time_taken_sec) values('{}',{},{})".format(uid,scre,tim)
        cursor.execute(comd)
        mycon.commit()

        
    def check():
        global cond,cl,scre,s,inp
        inp=en.get()
        try:
            
            if s==int(inp):
                scre+=5
                num()
            else:
                cond=False
                close()
        except ValueError:
            pass
        
        
        
    def num():
        global s,cond
        a=r.randint(1,100)
        b=r.randint(1,100)
        lb1["text"]=a,"+",b
        s=a+b
        en.delete(0,tk.END)
        cond=True
        

    def handle_click(event):
        check()

    mw.destroy()
    tim=0
    scre=0
    win=tk.Tk()
    lb=tk.Label(text="",height=2,font=("Consolas",23,"bold"),width=30,bg="#C766D7")
    lb.grid(row=0,column=0)
    lb1=tk.Label(text="",
                 height=2,font=("Consolas",23,"bold"),width=30,bg="#C766D7")
    lb1.grid(row=1,column=0)
    en=tk.Entry(font=("Consolas",23,"bold"),width=30,bg="#87FEF4")
    en.grid(row=2,column=0)
    def focus_entry():
        en.focus_force()
    win.after(200,focus_entry)
    win.bind("<Return>", handle_click)
    
    num()
    thr=threading.Thread(target=timer)
    thr.start()
    win.mainloop()
    
def typing():
    global tim,type_correct
    def close():
        win.destroy()
        print("Time taken:",tim)
        scre=type_correct*5
        print("Score:",scre)
        
        cursor.execute("select * from type_leaderboard")
        data=cursor.fetchall()
        names={}
        for i in data:
            names[i[0]]=(i[1],i[2])
            
        if uid in names:
            if names[uid][0]<scre or (names[uid][0]==scre and names[uid][1]>tim):
                comd="update type_leaderboard set score={},time_taken_sec={} where userid='{}'".format(scre,tim,uid)
            else:
                comd=""
        elif uid=="" and scre==0 and tim==0:#i.e the user closes the enter username window
            comd=""

        else:
            comd="insert into type_leaderboard(userid,score,time_taken_sec) values('{}',{},{})".format(uid,scre,tim)
        cursor.execute(comd)
        mycon.commit()


    def timer():
        global t,tim
        t=60
        while True:
            try:
                    lb["text"]=t
                    win.update()
                
                
                    t-=1
                    
                    if t<0:
                        time.sleep(0.5)
                        close()
                        break 
                    if cond==False:
                        break
                    
            except RuntimeError:
                    pass
                
            tim+=1
            time.sleep(1)

    def sent():
        global line
        if l:
            line=r.choice(l)
            l.remove(line)
            lb1["text"]=line
        else:
            close()
        

    def check():
        global type_correct,cond
        inp=en.get()
        en.delete(0,tk.END)
        if inp==line:
            type_correct+=1
            sent()
        else:
            close()
        

    def handle_click(event):
        check()

    mw.destroy()
    tim=0
    type_correct=0
    cond=True
    myfile=open(r'C:\Users\HP\OneDrive\Desktop\Computer Science Proj\text file\sentences.txt',"r")
    s=" "
    l=[]
    while s:
        s=myfile.readline().strip()
        if s!="":
            l.append(s)
    myfile.close()
    
    win=tk.Tk()
    lb=tk.Label(text="",height=2,font=("Consolas",23,"bold"),width=30,bg="#C766D7")
    lb.grid(row=0,column=0)
    lb1=tk.Label(text="",
                 height=2,font=("Consolas",23,"bold"),width=30,bg="#C766D7")
    lb1.grid(row=1,column=0)
    en=tk.Entry(font=("Consolas",23,"bold"),width=30,bg="#87FEF4")
    en.grid(row=2,column=0)
    def focus_entry():
        en.focus_force()
    win.after(200,focus_entry)
    win.bind("<Return>", handle_click)
    
    sent()
    thr=threading.Thread(target=timer)
    thr.start()
    win.mainloop()    

def maths_lb():
    mw.destroy()
    cursor.execute("select * from maths_leaderboard order by score desc,time_taken_sec asc,userid asc")
    data=cursor.fetchall()
    
    head="{:<10} {:<20} {:<20} {:<20}".format("RANK","USERID","SCORE","TIME")
    print(head)
    print("-"*70)
    rnk=0
    for i in range(len(data)):
        rnk+=1
        if i>0:
            if data[i][1]==data[i-1][1] and data[i][2]==data[i-1][2]:
                rnk-=1
        text="{:<10} {:<20} {:<20} {}".format(rnk,data[i][0],data[i][1],data[i][2])
        print(text)

def type_lb():
    mw.destroy()
    cursor.execute("select * from type_leaderboard order by score desc,time_taken_sec asc,userid asc")
    data=cursor.fetchall()
    
    head="{:<10} {:<20} {:<20} {:<20}".format("RANK","USERID","SCORE","TIME")
    print(head)
    print("-"*70)
    rnk=0
    for i in range(len(data)):
        rnk+=1
        if i>0:
            if data[i][1]==data[i-1][1] and data[i][2]==data[i-1][2]:
                rnk-=1
        text="{:<10} {:<20} {:<20} {}".format(rnk,data[i][0],data[i][1],data[i][2])
        print(text)

def overall_lb():
    mw.destroy()
    print("Play both Speed Maths and Speed Typing to appear on the Overall Leaderboard!")
    print()
    cmd="select m.userid,m.score+t.score from maths_leaderboard m,type_leaderboard t where m.userid=t.userid"
    cursor.execute(cmd)
    data=cursor.fetchall()
    
    head="{:<30} {:<20}".format("RANK","USERID","TOTAL SCORE")
    print(head)
    print("-"*70)
    rnk=0
    for i in range(len(data)):
        rnk+=1
        if i>0:
            if data[i][1]==data[i-1][1]:
                rnk-=1
        text="{:<30} {:<20}".format(rnk,data[i][0],data[i][1])
        print(text)

def game_stats():
    mw.destroy()
    print("Your best score and time is considered for the leaderboard!")
    print()
    print("SPEED MATHS")
    cmd="select score,time_taken_sec from maths_leaderboard where userid='{}'".format(uid)
    cursor.execute(cmd)
    data=cursor.fetchone()
    if data:
        print("Score:",data[0])
        print("Time taken(in sec):",data[1])
    else:
        print("You haven't played speed maths yet. Give it a try!")
        
    print()    
    print("SPEED TYPING")
    cmd="select score,time_taken_sec from type_leaderboard where userid='{}'".format(uid)
    cursor.execute(cmd)
    data=cursor.fetchone()
    if data:
        print("Score:",data[0])
        print("Time taken(in sec):",data[1])
    else:
        print("You haven't played speed typing yet. Give it a try!")
    
    
def next_step():
    global mw
    mw=tk.Tk()
    mw.configure(bg="#5483FA")
    txt_user="Welcome {} !".format(uid)
    wel=tk.Label(text=txt_user,font=("Consolas",23,"bold"),bg="#5483FA")
    wel.grid(row=0,column=0)
    play1=tk.Button(text="Play Speed Maths",command=maths,width=50,height=2,font=("Consolas",20,"bold"),bg="#F486F4")
    play1.grid(row=1,column=0,padx=10,pady=10,sticky="nsew")#F486F4
    play2=tk.Button(text="Play Speed Typing",command=typing,width=50,height=2,font=("Consolas",20,"bold"),bg="#B0F2F7")
    play2.grid(row=2,column=0,padx=10,pady=10,sticky="nsew")
    leabrd1=tk.Button(text="Check Maths Leaderboard",command=maths_lb,width=50,height=2,font=("Consolas",20,"bold"),
                     bg="#F48688")
    leabrd1.grid(row=3,column=0,sticky="nsew",padx=10,pady=10)
    leabrd2=tk.Button(text="Check Typing Leaderboard",command=type_lb,width=50,height=2,font=("Consolas",20,"bold"),
                     bg="#5CE886")
    leabrd2.grid(row=4,column=0,sticky="nsew",padx=10,pady=10)
    leabrd_all=tk.Button(text="Check Overall Leaderboard",command=overall_lb,width=50,height=2,font=("Consolas",20,"bold"),
                     bg="#E5AD90")
    leabrd_all.grid(row=5,column=0,sticky="nsew",padx=10,pady=10)
    check_score=tk.Button(text="Check My Game Stats",command=game_stats,width=50,height=2,font=("Consolas",20,"bold"),
                     bg="#E5E090")
    check_score.grid(row=6,column=0,sticky="nsew",padx=10,pady=10)
    mw.mainloop()

def playn():
    global uid,en_na,tt2,mw,tt1,play
    uid=en_na.get()
    if uid=="":
        tt2['text']="Please enter a UserId"
    
    else:
        
        cmd="select score from maths_leaderboard where userid='{}'".format(uid)
        cursor.execute(cmd)
        data_m=cursor.fetchone()
        cmd="select score from type_leaderboard where userid='{}'".format(uid)
        cursor.execute(cmd)
        data_t=cursor.fetchone()
        if data_m==None and data_t==None :
            mw.destroy()
            next_step()
        else:
            tt2['text']="UserID already exists!"

def n_user():
    global mw,en_na,tt1,tt2
    mw.destroy()
    mw=tk.Tk()
    mw.configure(bg="#5483FA")
    tt1=tk.Label(text="Enter Unique UserID (Note:UserId isn't case sensitive)",width=50,height=2,font=("Consolas",20,"bold"),bg="#FAB439")
    tt1.grid(row=1,column=0,padx=20,pady=20,sticky="nsew")
    tt2=tk.Label(text="",width=50,height=1,font=("Consolas",20,"bold"),bg="#5483FA")
    tt2.grid(row=2,column=0,padx=20,pady=20,sticky="nsew")
    en_na=tk.Entry(width=50,font=("Consolas",23,"bold"),bg="#EBB6AC")
    en_na.grid(row=3,column=0,padx=20,pady=20,sticky="nsew")
    nextt=tk.Button(text="Play",command=playn,width=50,height=1,font=("Consolas",23,"bold"),bg="#FAB439")
    nextt.grid(row=7,column=0,padx=20,pady=20,sticky="nsew")
    mw.mainloop()

def playo():
    global uid
    uid=en_id.get()
    if uid=="":
        tt2['text']="Please enter a UserId"
    else:
        
        cmd="select score from maths_leaderboard where userid='{}'".format(uid)
        cursor.execute(cmd)
        data_m=cursor.fetchone()
        cmd="select score from type_leaderboard where userid='{}'".format(uid)
        cursor.execute(cmd)
        data_t=cursor.fetchone()
        if data_m==None and data_t==None:
            tt2['text']="UserID not found!"
        else:
            mw.destroy()
            next_step()
    
def o_user():
    global mw,en_id,tt2
    mw.destroy()
    mw=tk.Tk()
    mw.configure(bg="#5483FA")
    tt1=tk.Label(text="Enter your UserID (Note:UserId isn't case sensitive)",width=50,height=2,font=("Consolas",20,"bold"),bg="#9DF753")
    tt1.grid(row=1,column=0,padx=20,pady=20,sticky="nsew")
    tt2=tk.Label(text="",width=50,height=1,font=("Consolas",23,"bold"),bg="#5483FA")
    tt2.grid(row=2,column=0,padx=20,pady=20,sticky="nsew")
    en_id=tk.Entry(width=50,font=("Consolas",23,"bold"),bg="#B4EBAC")
    en_id.grid(row=3,column=0,padx=20,pady=20,sticky="nsew")
    play=tk.Button(text="Play",command=playo,width=50,height=1,font=("Consolas",23,"bold"),bg="#9DF753")
    play.grid(row=4,column=0,padx=20,pady=20,sticky="nsew")
    
    
    
    mw.mainloop()

mw=tk.Tk()
mw.configure(bg="#5483FA")
mw.title('Speed Game')
ttl=tk.Label(text="SPEED GAME",font=("Consolas",27,"bold"),bg="#5483FA")
ttl.grid(row=0,column=0)
wel=tk.Label(text="Welcome! Are you an old user or new user?",font=("Consolas",23,"bold"),bg="#5483FA")
wel.grid(row=1,column=0)
new_user=tk.Button(text="New user",command=n_user,width=50,height=2,
                       font=("Consolas",23,"bold"),bg="#FAB439")
new_user.grid(row=2,column=0,padx=20,pady=20,sticky="nsew")
old_user=tk.Button(text="Old user",width=50,height=2,font=("Consolas",23,"bold"),command=o_user,
                     bg="#9DF753")
old_user.grid(row=3,column=0,sticky="nsew",padx=20,pady=20)
mw.mainloop()
