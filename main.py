
from menu import show_menu
from student_info import *
def main():
    docs=[]
    while True:
        show_menu()
        s=input('請選擇:')
        if s=="1":
            docs += input_student()
        elif s=="2":
            output_student(docs)
        elif s=="3":
            modify_student_info(docs)
        elif s=="4":
            delete_student_info(docs)
        elif s=='5':
            print_by_score_desc(docs)
        elif s=="6":
            print_by_score_asc(docs)
        elif s=='7':
            print_by_age_desc(docs)
        elif s=='8':
            print_by_age_asc(docs)
        elif s=="9":
            save_to_file(docs)
        elif s=="10":
            docs=read_from_file()
        elif s=='q':
            return

main()