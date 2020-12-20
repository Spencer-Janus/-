def assessment(grade):
    num=0
    f=open("grades.txt","r")
    list_=f.readlines()
    list_grade=[float(i.replace('\n','')) for i in list_]
    for i in list_grade:
        if grade>i:
            num=num+1
    return round(num/len(list_grade)*100,1)