class Student:
    count=0
    def __init__(self,name,age,score=0):
        self.__name=name
        self.__age=age 
        self.__score=score
        Student.count+=1
    def __del__(self):
        Student.count-=1
    def get_age(self):
        return self.__age
    def get_score(self):
        return self.__score
    def set_score(self,score):
        if 0<=score<=100:
            self.__score=score
            return
        raise ValueError('成績有誤'+str(score))

    def get_infos(self):
        return (self.__name,self.__age,self.__score)
    def is_name(self,n):
        return self.__name==n

    def write_to_file(self, file):
        file.write(self.__name)
        file.write(',')
        file.write(str(self.__age))
        file.write(',')
        file.write(str(self.__score))
        file.write('\n')
        
    @classmethod
    def getTotalcount(cls):
        return cls.count


def test():
    L=[]
    L.append(Student('Leon',20,100))
    L.append(Student('Huang',18,90))
    L.append(Student('Jun',19,80))
    print('學生數為:',Student.getTotalcount())
    L2=[]
    L2.append(Student('Lyon',18,90))
    print(Student.getTotalcount())
    L.pop(1)
    print('學生數為:',Student.getTotalcount())
    all_student=L+L2
    score=0
    for s in all_student:
        score+=s.get_score()
    print('平均成績為:',score/len(all_student))
if __name__=='__main__':
    test()