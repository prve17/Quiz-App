#imports

import random,sys
from tkinter import *
from tkinter.ttk import Separator
from tkinter.messagebox import showinfo
from time import time,strftime
#Window

root=Tk()
root.geometry('700x500')
root.resizable(0,0)
root.title('QUIZ APP')

root.config(bg='White')
i=0
timeLeft={'min':2,'sec':5}
intro= '''\t\t :: Instructions ::
      <><><><><><><><><><><><><><><><><><><><>
          1. Total Quiz Time is : 02:00 Min
          2. Total questions : 02
          3. Total Score : 04 x 100 =400
                as you have only one chance to select.
          \t\t Good Luck!!
      <><><><><><><><><><><><><><><><><><><><>
'''
print(intro)

def timeShow():
    global i,timeLeft
    if timeLeft['min']==2 and timeLeft['sec']>0:
        note.config(text='You can start Quiz after {} Seconds.'.format(timeLeft['sec']))
        timeLeft['sec']-=1
    elif timeLeft['sec']>0:
        submit.config(state=NORMAL)
        instruction.config(text='')
        timeLeft['sec']-=1
        note.config(text='Time left: {}min:{}sec'.format(timeLeft['min'],timeLeft['sec']))
    elif timeLeft['min']!=0 and timeLeft['sec']==0:
        timeLeft['min']-=1
        timeLeft['sec']=59
        note.config(text='Time left: {}min:{}sec'.format(timeLeft['min'],timeLeft['sec']))
    elif timeLeft['min']==0 and timeLeft['sec']==0:
        print('Time up!')
        result()
    showtime.config(text=strftime('%H:%M:%S'))
    showtime.after(1000,timeShow)

#Attendance

def getDetails():
    global name,roll,mainWindow,Name,Roll
    Name=name.get()
    Roll=roll.get()
    root.deiconify()
    timeShow()
    mainWindow.destroy()

def attendance():
    global name,roll,mainWindow
    mainWindow=Toplevel(root)
    mainWindow.geometry('700x500')
    mainWindow.resizable(0,0)
    mainWindow.title('QUIZ APP')
    #mainWindow.tk.call(img)
    mainWindow.config(bg='white')

    #app name same as root

    appName=Label(mainWindow,text=title,font=('impact',20,'italic'),
                  justify=CENTER,bg='blue',fg='black')
    appName.pack(side=TOP,fill=BOTH)

    #label to show info of attendance

    info=Label(mainWindow,text="Enter Your Name and Rollno.",bg='white',fg='sky blue',font=('arial',15))
    info.place(x=210,y=200)
    name=Entry(mainWindow,width=30)
    name.place(x=250,y=235)
    roll=Entry(mainWindow,width=30)
    roll.place(x=250,y=260)
    name.insert(END,'Name')
    roll.insert(END,'Roll')
    submit=Button(mainWindow,text='Confirm & Start',width=20,bg='sky blue',fg='green',command=getDetails)
    submit.place(x=265,y=300)
    mainWindow.mainloop()

#Toplevel finish

#Quit quiz

def quit_function():
    answer = showinfo(message="Try next time")
    if answer=='ok':
        sys.exit(root.destroy())

#Disable all Button

def dis_button():
    option1.config(state=DISABLED)
    option2.config(state=DISABLED)
    option3.config(state=DISABLED)
    option4.config(state=DISABLED)

#Enable all Button

def en_button():
    option1.config(state=NORMAL)
    option2.config(state=NORMAL)
    option3.config(state=NORMAL)
    option4.config(state=NORMAL)

#Show final result

def result():
    global score,Name,Roll
    root.withdraw()
    top=Toplevel(root)
    #top.tk.call('wm','iconphoto',top._w,PhotoImage(file=''))
    top.geometry('200x100')
    top.resizable(0,0)
    top.title('QUIZ RESULT')
    top.config(bg='sky blue')
    top.protocol('WM_DELETE_WINDOW',quit_function)
    filename=Name+'_'+Roll+'.txt'
    data='\nStudent:'+Name+'\nRoll:'+Roll+'\nScore: '+str(score)+'\nCompleted quiz at : '+strftime('%d/%m/%y --%H:%M:%S')
    with open(filename,'a') as file:
        file.write(data)
    label=Label(top,text='QUIZ OVER...\n Score: '+str(score),font=30,fg='black',bg='sky blue').place(x=50,y=25)
    exitBtn=Button(top,text='Exit',width=10,bg='white',fg='green',command=quit_function).place(x=50,y=70)
    top.mainloop()

#questions and corresponding answers

questions={" What is the 16-bit compiler allowable range for integer constants?":'-32768 to 32767',
           'What is required in each C program?':'at least one function.',
           '''main(){  
  int i = 2;{  
    int i = 4, j = 5;  
     printf("%d %d", i, j);}    
  printf("%d %d", i, j);}''':'4525',
           'What is a lint?':'Analyzing tool'}

#separate Questions and answers  from questions variable

que=[]
ans=[]
for key,value in questions.items():
    que.append(key)
    ans.append(value)

#corresponding answers with answers including at random

options=[
    ['-3.4e38 to 3.4e38','-32767 to 32768','-32668 to 32667',ans[0]],
    [ans[1],'any function.','Input data','Output data'],
    [ans[2],'2525','4545','NOT'],
    ['C compiler','Interactive debugger',ans[3],'C interpreter']
        ]
#_____________________________________________
currentQ=''
queNo=None
currentA=''
score=0
qn=1
var=StringVar()
def _next():
    global currentQ,currentA,queNo,score,i,qn
    i=0

    #till last question is left

    if len(que)>0:
        currentQ=random.choice(que)
        print(currentQ)
        q=Label(root,text='Que. '+str(qn),font=('arial',10)).place(x=20,y=80)
        qn+=1
        #______________________________________
        queNo=que.index(currentQ)
        print(options[queNo])
        currentA=questions[currentQ]
        #firstly change caption of button

        submit.config(text='Next')

        #print current question on quelabel

        queLabel.config(text=currentQ,fg='green',height=6)

        #print options for Questions on labels--- option 1,option2,.....

        en_button()
        option1.config(text=options[queNo][0],bg='sky blue',value=options[queNo][0],bd=1,command=answer)
        option2.config(text=options[queNo][1], bg='sky blue', value=options[queNo][1], bd=1, command=answer)
        option3.config(text=options[queNo][2], bg='sky blue', value=options[queNo][2], bd=1, command=answer)
        option4.config(text=options[queNo][3], bg='sky blue', value=options[queNo][3], bd=1, command=answer)

        #remove question from list which are asked

        que.remove(currentQ)
        ans.remove(currentA)
        options.remove(options[queNo])
    elif len(que)==0:
        result()
def answer():
    global currentQ,currentA,score

    #print selected radiobutton

    a= var.get()
    if currentA==str(a):
        score+=100
        dis_button()
    else:
        dis_button()
title='''C programming Questions'''
appName=Label(root,text=title,font=('impact',20,'italic'),
              justify=CENTER,bg='blue',fg='black')
appName.pack(side=TOP,fill=BOTH)
s=Separator(root).place(x=0,y=195,relwidth=1)
#label to show current question

queLabel=Label(root,text='',justify=LEFT,font=25)
queLabel.pack(side=TOP,fill=BOTH)
s=Separator(root).place(x=0,y=195,relwidth=1)

#options label

option1=Radiobutton(root,text='',bg='white',font=20,width=20,relief=FLAT,indicator=0,value=1,variable=var,bd=0)
option1.place(x=150,y=250)
option2=Radiobutton(root,text='',bg='white',font=20,width=20,relief=FLAT,indicator=0,value=2,variable=var,bd=0)
option2.place(x=400,y=250)
option3=Radiobutton(root,text='',bg='white',font=20,width=20,relief=FLAT,indicator=0,value=3,variable=var,bd=0)
option3.place(x=150,y=300)
option4=Radiobutton(root,text='',bg='white',font=20,width=20,relief=FLAT,indicator=0,value=4,variable=var,bd=0)
option4.place(x=400,y=300)

#instructions of Quiz

instruction=Label(root,text=intro,bg='sky blue',fg='white',font=('calibri',15),justify=LEFT)
instruction.place(x=150,y=200)

#note to quiz

note=Label(root,text='',font=('impact',10),bg='black',fg='green')
note.pack(side=BOTTOM)

#submit button

submit=Button(root,text='Start Quiz',font=('impact',15),fg='white',bg='blue',state=DISABLED,command=_next)
submit.pack(side=BOTTOM)

#show current time

showtime=Label(root,text='',font=20,fg='black',bg='sky blue')
showtime.place(x=620,y=50)

#progress bar for time left for each question

if __name__=="__main__":
    root.withdraw()
    attendance()
    root.mainloop()
