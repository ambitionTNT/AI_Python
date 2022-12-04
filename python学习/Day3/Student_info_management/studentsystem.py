# python learing
# author:TNT
import  os

filename='student.txt'
def main():
    while True:
        menm()
        choice=int(input('请选择'))
        if choice in[0,1,2,3,4,5,6,7]:
            if choice==0:
                answer=input('您确定要退出系统吗？y/n')
                if answer=='y' or answer =='n':
                    print('谢谢您的使用！！！！')
                    break
                else:
                    continue
            elif choice == 1:
                insert()#录入学生信息
            elif choice == 2:
                search()#查询学生信息
            elif choice == 3:
                delete() #删除学生信息
            elif choice == 4:
                modify() #修改学生信息
            elif choice == 5:
                sort() #排序
            elif choice ==6:
                total() #统计
            elif choice ==7:
                show() #显示所有学生信息



def menm():
    print("==========================学生信息管理系统==================================")
    print('----------------------------功能菜单-------------------------------------')
    print('\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t5.排序')
    print('\t\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t\t0.退出系统')
    print('--------------------------------------------------------------------------------------') ,

def insert():
    student_list = []
    while True:
        id=input('请输入学生的id（如10001)')
        if not id:
            break
        name=input('请输入学生的姓名')
        if not name:
            break
        try:
            English=input('请输入英语成绩')
            math=input('请输入数学成绩')
            python=input('请输入python成绩')
        except:
            print('输入无效，不是整数，请重新输入')
            continue
        #将学生信息保存字字典中
        student={'id':id,'name':name,'English':English,'math':math,'Python':python}
        student_list.append(student)
        answer=input('是否继续添加？n/y\n')
        if answer=='y':
            continue
        else:
            break
    save(student_list)
    print('学生信息录入完毕！！！')

def save(lst):
    try:

        stu_txt=open(filename,'a',encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')

    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()



def search():
    student_query=[]
    while True:
        id=''
        name=''
        if os.path.exists(filename):
            mode=input('按ID查找请输入1，按姓名查找请输入2')
            while True:

                if mode=='1':
                    id=input('请输入学生ID')
                    break
                elif mode=='2':
                    name=input('请输入学生姓名')
                    break
                else:
                    print('您输入的有误，请重新输入')
                    continue
            with open(filename,'r',encoding='utf-8') as rfile:
                student=rfile.readlines()
                for item in student:
                    d=dict(eval(item))
                    if id!='':
                        if id==d['id']:
                            student_query.append(d)
                    elif name!='':
                        if name==d['name']:
                            student_query.append(d)
            show_student(student_query)
            answer=input('是否继续（y/n）')
            if answer=='y':
                continue
            else:
                return

        else:
            print('暂未存入数据')
            return
def show_student(lst):
    if len(lst)==0:
        print('无数据')
        return
    #定义标题显示格式
    format_list='{:^6}\t{:^12}\t{:^10}\t{:^10}\t{:^9}\t{:^10}'
    print(format_list.format('ID','姓名','英语成绩','数学成绩','python成绩','总成绩'))
    #定义内容显示格式
    format_data='{:^6}\t{:^12}\t{:^13}\t{:^13}\t{:^12}\t{:^10}'
    for item in lst:
        print(format_data.format(item['id'],

                                item.get('name'),

                                item.get('English'),
                                item.get('math'),

                                item.get('Python'),
                                int(item.get('English'))+int(item.get('math'))+int(item.get('Python'))
                                ))






def delete():
    while True:
        stu_id=input('请输入删除的学生ID')
        if   stu_id!='':
            if os.path.exists(filename):
                with open(filename,'r',encoding='utf-8') as file:
                    stu_old=file.readlines()#读取学生的信息
            else:
                stu_old=[]
            flag=False
            if stu_old:
                with open(filename, 'w',encoding='utf-8') as wfile:
                    d = {}
                    for item in stu_old:
                        d=dict(eval(item))
                        if d['id']!=stu_id:
                            wfile.write(str(d)+'\n')
                        else:
                            flag=True
                    if flag:
                        print('删除成功')
                    else:
                        print('没有找到信息')
            else:
                print('无任何信息')
                break
            show()
            answer=input('是否继续删除(y/n)')
            if answer=='y':
                continue
            else:
                break




def modify():

    show()
    #判断学生信息是否存在
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            stu_old = rfile.readlines()  # 读取学生的信息
    else:
        return
    while True:
        stu_id=input('请输入要修改的学生的ID')
        if stu_id !='':
            with open(filename,'w',encoding='utf-8') as wfile:
                for item in stu_old:
                    d=dict(eval(item))
                    if d['id']==stu_id:
                        print('找到信息，请修改')
                        while True:
                            try:
                                d['name']=input('请输入姓名')
                                d['English']=input('请输入英语成绩')
                                d['math']=input('请输入数学成绩')
                                d['python']=input('请输入python成绩')
                            except:
                                print('输入有误,请重新输入')
                            else:
                                break
                        wfile.write(str(d)+'\n')
                        print('修改成功')
                    else:
                        wfile.write(str(d)+'\n')
            answer=input('是否需要继续修改其他学生信息（y/n）')
            if answer=='y':
                modify()
            else:
                break





def sort():
    student_new=[]
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8')as rfile:
            student=rfile.readlines()

            for item in student:
                d=dict(eval(item))
                student_new.append(d)
    else:
        print('不存在文件')
        return
    asc_or_desc=input('请选择（0:升序 1：降序）')
    if asc_or_desc=='0':
        asc_or_desc=False
    elif asc_or_desc=='1':
        asc_or_desc=True
    else:
        print('您的输入有问题 请重新输入')
        sort()
    mode=input('请选择排序方式（1：按英语程序排序 2：按math成绩排序 3：按python成绩排序 4：按总成绩排序）')
    if mode=='1':
        student_new.sort(key=lambda x:int(x['English']),reverse=asc_or_desc)
    elif mode == '2':
        student_new.sort(key=lambda x:int(x['math']),reverse=asc_or_desc)
    elif mode =='3':
        student_new.sort(key=lambda x:int(x['Python']),reverse=asc_or_desc)
    elif mode=='4':
        student_new.sort(key=lambda x:int(x['English'])+int(x['math'])+int(x['Python']),reverse=asc_or_desc)
    else:
        sort()
    show_student(student_new)




def total():
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            student=rfile.readlines()
            if student:
                print(f'一共有{len(student)}名学生')
            else:
                print('还没有录入学生数据')
    else:
        print('再无存储数据')
        return

def show():
    student_list=[]
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            student=rfile.readlines()
            for item in student:
                student_list.append(eval(item))
            if student_list:
                show_student(student_list)

    else:
        print('没有数据')
        return

if __name__ == '__main__':
    main()

















