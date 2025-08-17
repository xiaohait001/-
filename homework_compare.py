name=""
hm=""
killer_file=""
num_word=open("词库.txt",'r',encoding="utf-8")
num_word=[num_word.strip() for num_word in num_word.readlines()]

def random_name(x,y,z):
    global name
    from random import randint
    r=int(randint(0,4))
    if r==0:
        name+=z
    if r==1:
        name+=str(x)
        name+=str(y)
        name+=str(z)
    if r==2:
        name+=str(x)
        name+="."
        name+=str(y)
        name+=str(z)
    if r==3:
        name+=str(num_word[int(x)*2-1])+str(num_word[int(y)*2-1])
        name+=z
    if r==4:
        name+=str(y)+"班"
        name+=z
class Homework:
    def homework(x):
        global hm
        if bool(x)==True:
            hm=open("homework True.py","r",encoding="utf-8")
            hm=hm.readlines()
        if bool(x)==False:
            hm=open("homework False.py","r",encoding="utf-8")
            hm=hm.readlines()
    def killer():
        global killer_file
        killer_file=open("haiter_killer.py","r",encoding="utf-8")
        killer_file=killer_file.readlines()
