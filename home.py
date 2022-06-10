from msilib.schema import ListBox
import socket
import time
import threading
from tkinter import *
from tkinter import Tk


root=Tk()
root.geometry("300x600")
root.config(bg="white")

def func():
    t = threading.Thread(target=recv)
    t.start()

def recv():
    listensocket = socket.socket()
    port=3050
    maxconnection=99
    ip=socket.gethostname()
    print(ip)

    listensocket.bind(('',port))
    listensocket.listen(maxconnection)
    (clientsocket,address) = listensocket.accept()

    while True:
        sendermessage = clientsocket.recv(1024).decode()
        if not sendermessage=="":
            time.sleep(5)
            lstbx.insert(0,"client : "+sendermessage)

s=0

def sendmsg():
    global s
    if s==0:
        s=socket.socket()
        hostname='DESKTOP-7C42EV3'
        port=4050
        s.connect((hostname,port))
        msg=messagebox.get()
        lstbx.insert(0,"You : "+msg)
        s.send(msg.encode())
        s=s+1
    else:
        msg=messagebox.get()
        lstbx.insert(0,"You : "+msg)
        s.send(msg.encode())
def threadsendmsg():
    th=threading.Thread(target=sendmsg)
    th.start()

startchatimage = PhotoImage(file='start.png')
buttons = Button(root,image=startchatimage,command=func,borderwidth=0,width=200,height=50)
buttons.place(x=90,y=10)
buttons.pack(pady=30)
message = StringVar()
messagebox = Entry(root,textvariable=message,font=('calibre',10,'normal'),border=2,width=32)
messagebox.place(x=10,y=444)

sendmessageimg = PhotoImage(file='send.png')

sendmessagebutton=Button(root,image=sendmessageimg,command=threadsendmsg,borderwidth=0,width=150,height=50)
sendmessagebutton.place(x=90,y=500)


lstbx = Listbox(root,height=20,width=43)
lstbx.place(x=15,y=80)



root.mainloop()