import random
from test2 import *

'''
listblanks=[]
decimal_num=0  #是否有小数
Ifinclude=1    #是否有括号
scope=1000        #数的范围
variable_num=3 #数的个数
choose_num=4   #选择题个数
judge_num=3    #判断题个数
blank_num=3    #填空题个数
difficulty_num=2
'''
count=0
count_2=0
'''
decimal_num,Ifinclude,scope,variable_num,choose_num,judge_num,blank_num,difficulty_num


for i in range(1,100):
    index=random.randint(0,scope)
    while index in list_int:
        index = random.randint(0,scope )
    list_int.append(index)   
for i  in range(1,100):
    index1=round(random.uniform(0,scope),1)
    index2=random.randint(0,scope)
    while index1 in list_intafloat:
        index1 = round(random.uniform(0, scope),1)
    list_intafloat.append(index1)
    while index2 in list_intafloat:
        index2=index2=random.randint(0,scope)
    list_intafloat.append(index2)
print(list_int)
'''
'''

'''
'''
if difficulty_num==1:
    k=['+','-']
elif difficulty_num==2:
    k=['+','-','*','/','+','+','+','-','+','-','-']
list_int=[]
list_intafloat=[]
count=0
if scope==10:
    for i in range(11):
        list_int.append(i)
    for i in range(100):
        if i<60:
            list_intafloat.append(random.randint(0,10))
        else:
            list_intafloat.append(round((random.uniform(0,10)),1))
elif scope==100:
    for i in range(100):
        if i<70:
            list_int.append(random.randint(0,50))
        list_int.append(random.randint(50,101))
    for i in range(100):
        if i<70:
            list_intafloat.append(random.randint(0,50))
        else:
            list_intafloat.append(round((random.uniform(0,100)),1))
elif scope==1000:
    for i in range(100):
        if i<70:
            list_int.append(random.randint(0,101))
        elif i<90:
            list_int.append(random.randint(101,500))
        else:
            list_int.append((random.randint(500,1000)))
    for i in range(50):
        if i<40:
            list_intafloat.append(random.randint(0, 101))
            list_intafloat.append(round(random.uniform(0,101)))
        elif i<48:
            list_intafloat.append(random.randint(101, 500))
            list_intafloat.append(round(random.uniform(101,500)))



'''






def blankscalculate(decimal_num,Ifinclude,scope,variable_num,choose_num,judge_num,blank_num,difficulty_num,list_intafloat,list_int,k):
    print('填空题')
    print_text_("填空题",blank_num)
    f=open("question.txt","a")
    f.write("填空题："+'\n')
    if variable_num==2:     #先规定变量的个数
        if Ifinclude==0:       #选择是否有括号
            if decimal_num:   #选择是否有小数
                for i in range(0,blank_num):
                    a=str(random.choice(list_intafloat)) + random.choice(k) + str(random.choice(list_intafloat))
                    printblank(a,f)
            else:
                for i in range(0,blank_num):
                    a=str(random.choice(list_int)) + random.choice(k) + str(random.choice(list_int))
                    printblank(a,f)
        else:
            if decimal_num:   #选择是否有小数
                for i in range(0,blank_num):
                    a=str(random.choice(list_intafloat)) + random.choice(k) + str(random.choice(list_intafloat))
                    printblank(a,f)
            else:
                for i in range(0,blank_num):
                    a=str(random.choice(list_int)) + random.choice(k) + str(random.choice(list_int))
                    printblank(a,f)
    elif variable_num==3:
        if Ifinclude==0:
            if decimal_num:
                for i in range(0,blank_num):
                    b=str(random.choice(list_intafloat)) + random.choice(k) + str(random.choice(list_intafloat)) + random.choice(k) + str(random.choice(list_intafloat))
                    printblank(b,f)
            else:
                for i in range(0,blank_num):
                    b=str(random.choice(list_int)) + random.choice(k) + str(random.choice(list_int)) + random.choice(k) + str(random.choice(list_int))
                    printblank(b,f)
        else:
            if decimal_num:
                list_temporay = []
                for i in range(50):
                    list_temporay.append('(' + str(random.choice(list_intafloat)) + random.choice(k) + str(random.choice(list_intafloat)) + ')' + random.choice(k) + str(random.choice(list_intafloat)))
                    list_temporay.append(str(random.choice(list_intafloat)) + random.choice(k) + '(' + str(random.choice(list_intafloat)) + random.choice(k) + str(random.choice(list_intafloat)) + ')')
                for i in range(0,blank_num):
                    printblank(random.choice(list_temporay),f)
            else:
                list_temporay3 = []
                for i in range(50):
                    list_temporay3.append('(' + str(random.choice(list_int)) + random.choice(k) + str(random.choice(list_int)) + ')' + random.choice(k) + str(random.choice(list_int)))
                    list_temporay3.append(str(random.choice(list_int)) + random.choice(k) + '(' + str(random.choice(list_int)) + random.choice(k) + str(random.choice(list_int)) + ')')
                for i in range(0,blank_num):
                    printblank(random.choice(list_temporay3),f)
    elif variable_num==4:
        if Ifinclude==0:
            if decimal_num:
                for i in range(0,blank_num):
                    a=str(random.choice(list_intafloat))+random.choice(k)+str(random.choice(list_intafloat))+random.choice(k)+str(random.choice(list_intafloat))+random.choice(k)+str(random.choice(list_intafloat))
                    printblank(a,f)
            else:
                for i in range(0,blank_num):
                    a=str(random.choice(list_int))+random.choice(k)+str(random.choice(list_int))+random.choice(k)+str(random.choice(list_int))+random.choice(k)+str(random.choice(list_int))
                    printblank(a,f)
        else:
            if decimal_num:
                list_temporay1=[]
                for i in range(20):
                    list_temporay1.append('(' + str(random.choice(list_intafloat)) + random.choice(k) + str(random.choice(list_intafloat)) + ')' + random.choice(k) + str(random.choice(list_intafloat)) + random.choice(k) + str(random.choice(list_intafloat)))
                    list_temporay1.append( '(' + str(random.choice(list_intafloat)) + random.choice(k) + str(random.choice(list_intafloat)) + random.choice(k) + str(random.choice(list_intafloat)) + ')' + random.choice(k) + str(random.choice(list_intafloat)))
                    list_temporay1.append(str(random.choice(list_intafloat)) + random.choice(k) + '(' + str(random.choice(list_intafloat)) + random.choice(k) + str(random.choice(list_intafloat)) + ')' + random.choice(k) + str(random.choice(list_intafloat)))
                    list_temporay1.append(str(random.choice(list_intafloat)) + random.choice(k) + str(random.choice(list_intafloat)) + random.choice(k) + '(' + str(random.choice(list_intafloat)) + random.choice(k) + str(random.choice(list_intafloat)) + ')')
                    list_temporay1.append(str(random.choice(list_intafloat)) + random.choice(k) + '(' + str(random.choice(list_intafloat)) + random.choice(k) + str(random.choice(list_intafloat)) + random.choice(k) + str(random.choice(list_intafloat)) + ')')
                for i in range(0,blank_num):
                    printblank(random.choice(list_temporay1),f)
            else:
                list_temporay2=[]
                for i in range(10):
                    list_temporay2.append('(' + str(random.choice(list_int)) + random.choice(k) + str(random.choice(list_int)) + ')' + random.choice(k) + str(random.choice(list_int)) + random.choice(k) + str(random.choice(list_int)))
                    list_temporay2.append( '(' + str(random.choice(list_int)) + random.choice(k) + str(random.choice(list_int)) + random.choice(k) + str(random.choice(list_int)) + ')' + random.choice(k) + str(random.choice(list_int)))
                    list_temporay2.append(str(random.choice(list_int)) + random.choice(k) + '(' + str(random.choice(list_int)) + random.choice(k) + str(random.choice(list_int)) + ')' + random.choice(k) + str(random.choice(list_int)))
                    list_temporay2.append(str(random.choice(list_int)) + random.choice(k) + str(random.choice(list_int)) + random.choice(k) + '(' + str(random.choice(list_int)) + random.choice(k) + str(random.choice(list_int)) + ')')
                    list_temporay2.append(str(random.choice(list_int)) + random.choice(k) + '(' + str(random.choice(list_int)) + random.choice(k) + str(random.choice(list_int)) + random.choice(k) + str( random.choice(list_int)) + ')')
                for i in range(0,blank_num):
                    printblank(random.choice(list_temporay2),f)
    f.close()
def judge(decimal_num,Ifinclude,scope,variable_num,choose_num,judge_num,blank_num,difficulty_num,list_intafloat,list_int,k):
    print('判断题：回答T or F')
    print_text_("判断题",judge_num)
    f=open("question.txt","a")
    f.write("判断题："+'\n')
    if variable_num==2:     #先规定变量的个数
        if Ifinclude==0:       #选择是否有括号
            if decimal_num:   #选择是否有小数
                for i in range(0,judge_num):
                    a=str(random.choice(list_intafloat)) + random.choice(k) + str(random.choice(list_intafloat))

                    printjudgecal(a,f,list_intafloat)
            else:
                for i in range(0,judge_num):
                    a=str(random.choice(list_int)) + random.choice(k) + str(random.choice(list_int))
                    printjudgecal(a,f,list_intafloat)
        else:
            if decimal_num:   #选择是否有小数
                for i in range(0,judge_num):
                    a=str(random.choice(list_intafloat)) + random.choice(k) + str(random.choice(list_intafloat))
                    printjudgecal(a,f,list_intafloat)
            else:
                for i in range(0,judge_num):
                    a=str(random.choice(list_int)) + random.choice(k) + str(random.choice(list_int))
                    printjudgecal(a,f,list_intafloat)
    elif variable_num==3:
        if Ifinclude==0:
            if decimal_num:
                for i in range(0,judge_num):
                    b=str(random.choice(list_intafloat)) + random.choice(k) + str(random.choice(list_intafloat)) + random.choice(k) + str(random.choice(list_intafloat))
                    printjudgecal(b,f,list_intafloat)
            else:
                for i in range(0,judge_num):
                    b=str(random.choice(list_int)) + random.choice(k) + str(random.choice(list_int)) + random.choice(k) + str(random.choice(list_int))
                    printjudgecal(b,f,list_intafloat)
        else:
            if decimal_num:
                list_temporay = []
                for i in range(50):
                    list_temporay.append('(' + str(random.choice(list_intafloat)) + random.choice(k) + str(random.choice(list_intafloat)) + ')' + random.choice(k) + str(random.choice(list_intafloat)))
                    list_temporay.append(str(random.choice(list_intafloat)) + random.choice(k) + '(' + str(random.choice(list_intafloat)) + random.choice(k) + str(random.choice(list_intafloat)) + ')')
                for i in range(0,judge_num):
                    printjudgecal(random.choice(list_temporay),f,list_intafloat)
            else:
                list_temporay3 = []
                for i in range(50):
                    list_temporay3.append('(' + str(random.choice(list_int)) + random.choice(k) + str(random.choice(list_int)) + ')' + random.choice(k) + str(random.choice(list_int)))
                    list_temporay3.append(str(random.choice(list_int)) + random.choice(k) + '(' + str(random.choice(list_int)) + random.choice(k) + str(random.choice(list_int)) + ')')
                for i in range(0,judge_num):
                    printjudgecal(random.choice(list_temporay3),f,list_intafloat)
    elif variable_num==4:
        if Ifinclude==0:
            if decimal_num:
                for i in range(0,judge_num):
                    a=str(random.choice(list_intafloat))+random.choice(k)+str(random.choice(list_intafloat))+random.choice(k)+str(random.choice(list_intafloat))+random.choice(k)+str(random.choice(list_intafloat))
                    printjudgecal(a,f,list_intafloat)
            else:
                for i in range(0,judge_num):
                    a=str(random.choice(list_int))+random.choice(k)+str(random.choice(list_int))+random.choice(k)+str(random.choice(list_int))+random.choice(k)+str(random.choice(list_int))
                    printjudgecal(a,f,list_intafloat)
        else:
            if decimal_num:
                list_temporay1=[]
                for i in range(20):
                    list_temporay1.append('(' + str(random.choice(list_intafloat)) + random.choice(k) + str(random.choice(list_intafloat)) + ')' + random.choice(k) + str(random.choice(list_intafloat)) + random.choice(k) + str(random.choice(list_intafloat)))
                    list_temporay1.append( '(' + str(random.choice(list_intafloat)) + random.choice(k) + str(random.choice(list_intafloat)) + random.choice(k) + str(random.choice(list_intafloat)) + ')' + random.choice(k) + str(random.choice(list_intafloat)))
                    list_temporay1.append(str(random.choice(list_intafloat)) + random.choice(k) + '(' + str(random.choice(list_intafloat)) + random.choice(k) + str(random.choice(list_intafloat)) + ')' + random.choice(k) + str(random.choice(list_intafloat)))
                    list_temporay1.append(str(random.choice(list_intafloat)) + random.choice(k) + str(random.choice(list_intafloat)) + random.choice(k) + '(' + str(random.choice(list_intafloat)) + random.choice(k) + str(random.choice(list_intafloat)) + ')')
                    list_temporay1.append(str(random.choice(list_intafloat)) + random.choice(k) + '(' + str(random.choice(list_intafloat)) + random.choice(k) + str(random.choice(list_intafloat)) + random.choice(k) + str(random.choice(list_intafloat)) + ')')
                for i in range(0,judge_num):
                    printjudgecal(random.choice(list_temporay1),f,list_intafloat)
            else:
                list_temporay2=[]
                for i in range(10):
                    list_temporay2.append('(' + str(random.choice(list_int)) + random.choice(k) + str(random.choice(list_int)) + ')' + random.choice(k) + str(random.choice(list_int)) + random.choice(k) + str(random.choice(list_int)))
                    list_temporay2.append( '(' + str(random.choice(list_int)) + random.choice(k) + str(random.choice(list_int)) + random.choice(k) + str(random.choice(list_int)) + ')' + random.choice(k) + str(random.choice(list_int)))
                    list_temporay2.append(str(random.choice(list_int)) + random.choice(k) + '(' + str(random.choice(list_int)) + random.choice(k) + str(random.choice(list_int)) + ')' + random.choice(k) + str(random.choice(list_int)))
                    list_temporay2.append(str(random.choice(list_int)) + random.choice(k) + str(random.choice(list_int)) + random.choice(k) + '(' + str(random.choice(list_int)) + random.choice(k) + str(random.choice(list_int)) + ')')
                    list_temporay2.append(str(random.choice(list_int)) + random.choice(k) + '(' + str(random.choice(list_int)) + random.choice(k) + str(random.choice(list_int)) + random.choice(k) + str( random.choice(list_int)) + ')')
                for i in range(0,judge_num):
                    printjudgecal(random.choice(list_temporay2),f,list_intafloat)
    f.close()

def Choose(decimal_num,Ifinclude,scope,variable_num,choose_num,judge_num,blank_num,difficulty_num,list_intafloat,list_int,k):
    print('选择题')
    print_text_("选择题",choose_num)
    f=open("question.txt","a")
    f.write('选择题：' + "\n")
    if variable_num==2:     #先规定变量的个数
        if Ifinclude==0:       #选择是否有括号
            if decimal_num:   #选择是否有小数
                for i in range(0,choose_num):
                    a=str(random.choice(list_intafloat)) + random.choice(k) + str(random.choice(list_intafloat))

                    printchoose(a,f,list_intafloat)
            else:
                for i in range(0,choose_num):
                    a=str(random.choice(list_int)) + random.choice(k) + str(random.choice(list_int))
                    printchoose(a,f,list_intafloat)
        else:
            if decimal_num:   #选择是否有小数
                for i in range(0,choose_num):
                    a=str(random.choice(list_intafloat)) + random.choice(k) + str(random.choice(list_intafloat))
                    printchoose(a,f,list_intafloat)
            else:
                for i in range(0,choose_num):
                    a=str(random.choice(list_int)) + random.choice(k) + str(random.choice(list_int))
                    printchoose(a,f,list_intafloat)
    elif variable_num==3:
        if Ifinclude==0:
            if decimal_num:
                for i in range(0,choose_num):
                    b=str(random.choice(list_intafloat)) + random.choice(k) + str(random.choice(list_intafloat)) + random.choice(k) + str(random.choice(list_intafloat))
                    printchoose(b,f,list_intafloat)
            else:
                for i in range(0,choose_num):
                    b=str(random.choice(list_int)) + random.choice(k) + str(random.choice(list_int)) + random.choice(k) + str(random.choice(list_int))
                    printchoose(b,f,list_intafloat)
        else:
            if decimal_num:
                list_temporay = []
                for i in range(50):
                    list_temporay.append('(' + str(random.choice(list_intafloat)) + random.choice(k) + str(random.choice(list_intafloat)) + ')' + random.choice(k) + str(random.choice(list_intafloat)))
                    list_temporay.append(str(random.choice(list_intafloat)) + random.choice(k) + '(' + str(random.choice(list_intafloat)) + random.choice(k) + str(random.choice(list_intafloat)) + ')')
                for i in range(0,choose_num):
                    printchoose(random.choice(list_temporay),f,list_intafloat)
            else:
                list_temporay3 = []
                for i in range(50):
                    list_temporay3.append('(' + str(random.choice(list_int)) + random.choice(k) + str(random.choice(list_int)) + ')' + random.choice(k) + str(random.choice(list_int)))
                    list_temporay3.append(str(random.choice(list_int)) + random.choice(k) + '(' + str(random.choice(list_int)) + random.choice(k) + str(random.choice(list_int)) + ')')
                for i in range(0,choose_num):
                    printchoose(random.choice(list_temporay3),f,list_intafloat)
    elif variable_num==4:
        if Ifinclude==0:
            if decimal_num:
                for i in range(0,choose_num):
                    a=str(random.choice(list_intafloat))+random.choice(k)+str(random.choice(list_intafloat))+random.choice(k)+str(random.choice(list_intafloat))+random.choice(k)+str(random.choice(list_intafloat))
                    printchoose(a,f,list_intafloat)
            else:
                for i in range(0,choose_num):
                    a=str(random.choice(list_int))+random.choice(k)+str(random.choice(list_int))+random.choice(k)+str(random.choice(list_int))+random.choice(k)+str(random.choice(list_int))
                    printchoose(a,f,list_intafloat)
        else:
            if decimal_num:
                list_temporay1=[]
                for i in range(20):
                    list_temporay1.append('(' + str(random.choice(list_intafloat)) + random.choice(k) + str(random.choice(list_intafloat)) + ')' + random.choice(k) + str(random.choice(list_intafloat)) + random.choice(k) + str(random.choice(list_intafloat)))
                    list_temporay1.append( '(' + str(random.choice(list_intafloat)) + random.choice(k) + str(random.choice(list_intafloat)) + random.choice(k) + str(random.choice(list_intafloat)) + ')' + random.choice(k) + str(random.choice(list_intafloat)))
                    list_temporay1.append(str(random.choice(list_intafloat)) + random.choice(k) + '(' + str(random.choice(list_intafloat)) + random.choice(k) + str(random.choice(list_intafloat)) + ')' + random.choice(k) + str(random.choice(list_intafloat)))
                    list_temporay1.append(str(random.choice(list_intafloat)) + random.choice(k) + str(random.choice(list_intafloat)) + random.choice(k) + '(' + str(random.choice(list_intafloat)) + random.choice(k) + str(random.choice(list_intafloat)) + ')')
                    list_temporay1.append(str(random.choice(list_intafloat)) + random.choice(k) + '(' + str(random.choice(list_intafloat)) + random.choice(k) + str(random.choice(list_intafloat)) + random.choice(k) + str(random.choice(list_intafloat)) + ')')
                for i in range(0,choose_num):
                    printchoose(random.choice(list_temporay1),f,list_intafloat)
            else:
                list_temporay2=[]
                for i in range(10):
                    list_temporay2.append('(' + str(random.choice(list_int)) + random.choice(k) + str(random.choice(list_int)) + ')' + random.choice(k) + str(random.choice(list_int)) + random.choice(k) + str(random.choice(list_int)))
                    list_temporay2.append( '(' + str(random.choice(list_int)) + random.choice(k) + str(random.choice(list_int)) + random.choice(k) + str(random.choice(list_int)) + ')' + random.choice(k) + str(random.choice(list_int)))
                    list_temporay2.append(str(random.choice(list_int)) + random.choice(k) + '(' + str(random.choice(list_int)) + random.choice(k) + str(random.choice(list_int)) + ')' + random.choice(k) + str(random.choice(list_int)))
                    list_temporay2.append(str(random.choice(list_int)) + random.choice(k) + str(random.choice(list_int)) + random.choice(k) + '(' + str(random.choice(list_int)) + random.choice(k) + str(random.choice(list_int)) + ')')
                    list_temporay2.append(str(random.choice(list_int)) + random.choice(k) + '(' + str(random.choice(list_int)) + random.choice(k) + str(random.choice(list_int)) + random.choice(k) + str( random.choice(list_int)) + ')')
                for i in range(0,choose_num):
                    printchoose(random.choice(list_temporay2),f,list_intafloat)
    f.close()

def printblank(a,b):
    global count
    count=count+1
    Answer = open("answer.txt", 'a')
    question_t=open("questiontemporary.txt",'a')
    question_t.write(str(count)+': '+a+'='+'?'+'\n')
    print(a)
    answer=cal(a)
    b.write(str(count)+': '+a+'   '+answer+'\n')
    Answer.write(answer+'\n')
    Answer.close()
    question_t.close()
def printjudgecal(a,b,listc):
    global count
    count=count+1
    Answer = open("answer.txt", 'a')
    result = cal(a)
    listAnswer = []
    listAnswer.append(str(result))
    for i in range(3):
        listAnswer.append(random.choice(listc))
    question_t = open("questiontemporary.txt", 'a')
    d=random.choice(listAnswer)
    question_t.write(str(count)+ ': '+a +'='+str(d)+ '\n')
    if d==result:
        Answer.write("T"+'\n')
    else:
        Answer.write("F"+'\n')
    b.write(str(count)+': '+a+'   '+result+'\n')
    print(a+'='+str(random.choice(listAnswer)))
    Answer.close()
    question_t.close()
def printchoose(a,b,listc):
    global count
    count=count+1
    Answer=open("answer.txt",'a')
    question_t = open("questiontemporary.txt", 'a')
    question_t.write(str(count)+': '+a + '\n')
    result=cal(a)
    b.write(str(count) + ': ' + a+'   '+result + '\n')
    dict1 = {'A':'' , 'B': '', 'C': '','D': ''}
    list_letter=['A','B','C','D']
    correctAnswer=random.choice(list_letter)
    dict1[correctAnswer]=result
    list_letter.remove(correctAnswer)
    for i in list_letter:
        dict1[i]=random.choice((listc))
    print(a + '=' )
    for k,v in dict1.items():
        print(k+':'+str(v),end=' ')
        b.write(k+':'+str(v)+' ')
        question_t.write(k+':'+str(v)+' ')
    b.write('\n')
    question_t.write('\n')
    answer=cal(a)
    Answer.write(correctAnswer+'\n')
    Answer.close()
    question_t.close()
    print()


def print_text_(aaa,num):
    f=open("questiontemporary.txt","a")
    if num!=0:
        f.write(aaa+"\n")
    f.close()


#Choose()
#judge()
#blankscalculate()

