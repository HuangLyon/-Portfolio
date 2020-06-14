from student import Student
def input_student():
    L=[]
    while True:
        name=input('請輸入學生姓名:')
        if not name:
            break    

        age=int(input("請輸入年齡:"))
        score=int(input('請輸入成績:'))
        d=Student(name,age,score)
        L.append(d)
    return(L)
def output_student(L):
    print("+------------+------+-------+")
    print("|   name     | age  | score |")
    print("+------------+------+-------+")
    for d in L:
        n,a,s=d.get_infos()
        t=(n.center(12),
          str(a).center(6),
          str(s).center(7))
        line="|%s|%s|%s|"%t
        print(line)
    print("+------------+------+-------+")


def modify_student_info(lst):
    name = input('請輸入要修改的學生姓名:')
    for d in lst:
        if d.is_name(name):
            score=int(input('請輸入新的成績:'))
            d.set_score(score)
            print('修改',name,'的成績',score)
            return
    else:
        print('查無此人')

def delete_student_info(lst):
    name=input('請輸入要刪除的學生姓名:')
    for i in range(len(lst)):
        if lst[i].is_name(name):
            del lst[i]
            print('成功刪除:',name)
            return True
    else:
        print('查無此人')

def get_score(d):
    return d['score']
    
def get_age(d):
    return d['age']


def print_by_score_desc(lst):
    L=sorted(lst,key=lambda d:d.get_score(),reverse=True)
    output_student(L)


def print_by_score_asc(lst):
    L=sorted(lst,key=lambda d:d.get_score())
    output_student(L)

def print_by_age_desc(lst):
    L=sorted(lst,key=lambda d:d.get_age(),reverse=True)
    output_student(L)

def print_by_age_asc(lst):
    L=sorted(lst,key=lambda d:d.get_age())
    output_student(L)

def save_to_file(docs,filename='si.txt'):
    try:
        f=open(filename,'w')
        for stu in docs:
            stu.write_to_file(f)
        f.close()
        print('存檔成功')
    except OSError:
        print('存檔失敗')
def read_from_file(filename='si.txt'):
    L=[]
    try:
        f=open(filename)
        for line in f:
            s=line.rstrip()
            lst=s.split(',')
            name,age,score=lst 
            age=int(age)
            score=int(score)
            L.append(Student(name,age,score))
        f.close()
    except OSError:
        print('打開失敗')
    return L