import os
import re

filename = "student.txt"


def menu():
    print('=' * 18, '学生成绩管理系统', '=' * 18)
    print('-' * 23, '首页', '-' * 23)
    print('\t\t\t\t1、录入学生信息')
    print('\t\t\t\t2、查找学生信息 ')
    print('\t\t\t\t3、删除学生信息')
    print('\t\t\t\t4、修改学生信息')
    print('\t\t\t\t5、排序')
    print('\t\t\t\t6、统计学生总人数')
    print('\t\t\t\t7、显示所有学生信息')
    print('\t\t\t\t0、退出系统')
    print('-' * 50)
    print(' ' * 20, 'Tip:通过 数字 选择')


def main():
    ctrl = True
    while ctrl:
        menu()
        option = input('请选择:')
        option_str = re.sub("\D", "", option)
        if option_str in ['0', '1', '2', '3', '4', '5', '6', '7']:
            option_int = int(option_str)
            if option_int == 0:
                print(' 再会！')
                ctrl = False
            elif option_int == 1:
                insert()
            elif option_int == 2:
                search()
            elif option_int == 3:
                delete()
            elif option_int == 4:
                modify()
            elif option_int == 5:
                sort()
            elif option_int == 6:
                total()
            elif option_int == 7:
                show()


def insert():
    studentList = []
    mark = True
    while mark:
        s_id = input("请输入学生学号：")
        if not s_id:
            break
        name = input("请输入学生姓名：")
        if not name:
            break
        try:
            english = int(input("请输入英语成绩："))
            python = int(input("请输入Python成绩："))
            c = int(input("请输入C语言成绩："))
        except:
            print("输入无效，请重新录入")
            continue
        student = {"id": s_id, "name": name, "english": english, "python": python, "c": c}  # 将输入的学生信息保存到字典
        studentList.append(student)
        inputMark = input("是否继续添加？（y/n）:")
        if inputMark == "y":
            mark = True
        else:
            mark = False
    save(studentList)
    print("学生信息录入完毕！！！")


def save(student):
    try:
        students_txt = open(filename, "a")
    except Exception as e:
        students_txt = open(filename, "w")
    for info in student:
        students_txt.write(str(info) + "\n")
    students_txt.close()


def search():
    mark = True
    student_query = []
    while mark:
        s_id = ""
        name = ""
        if os.path.exists(filename):
            mode = input("按学号查查询输入1；按姓名查询输入2：")
            if mode == "1":
                s_id = input("请输入学生学号：")
            elif mode == "2":
                name = input("请输入学生姓名：")
            else:
                print("您的输入有误，请重新输入！")
                search()
            with open(filename, 'r') as file:
                student = file.readlines()
                for s_list in student:
                    d = dict(eval(s_list))
                    if s_id != "":
                        if d['id'] == s_id:
                            student_query.append(d)
                    elif name != "":
                        if d['name'] == name:
                            student_query.append(d)
                show_student(student_query)
                student_query.clear()
                inputMark = input("是否继续查询？（y/n）:")
                if inputMark == "y":
                    mark = True
                else:
                    mark = False
        else:
            print("暂未保存数据信息...")
            return


def delete():
    mark = True
    while mark:
        studentId = input("请输入要删除的学生学号：")
        if studentId != "":
            if os.path.exists(filename):
                with open(filename, 'r') as rfile:
                    student_old = rfile.readlines()
            else:
                student_old = []
            if_del = False
            if student_old:
                with open(filename, 'w') as w_file:
                    d = {}
                    for s_list in student_old:
                        d = dict(eval(s_list))
                        if d['id'] != studentId:
                            w_file.write(str(d) + "\n")
                        else:
                            if_del = True
                    if if_del:
                        print("学号为 %s 的学生信息已经被删除..." % studentId)
                    else:
                        print("没有找到ID为 %s 的学生信息..." % studentId)
            else:
                print("暂无学生信息...")
                break
            show()
            inputMark = input("是否继续删除？（y/n）:")
            if inputMark == "y":
                mark = True
            else:
                mark = False


def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r') as rfile:
            student_old = rfile.readlines()
    else:
        return
    student_id = input("请输入要修改的学生学号：")
    with open(filename, "w") as w_file:
        for student in student_old:
            d = dict(eval(student))
            if d["id"] == student_id:
                print("已查询到该学生的信息！")
                while True:
                    try:
                        d["name"] = input("请输入姓名：")
                        d["english"] = int(input("请输入英语成绩："))
                        d["python"] = int(input("请输入Python成绩："))
                        d["c"] = int(input("请输入C语言成绩："))
                    except:
                        print("您的输入有误，请重新输入。")
                    else:
                        break
                student = str(d)
                w_file.write(student + "\n")
                print("修改成功！")
            else:
                w_file.write(student)
    mark = input("是否继续修改其他学生信息？（y/n）：")
    if mark == "y":
        modify()


def sort():
    global ascORdescBool
    show()
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            student_old = file.readlines()
            student_new = []
        for s_list in student_old:
            d = dict(eval(s_list))
            student_new.append(d)
    else:
        return
    ascORdesc = input("请选择（0升序；1降序）：")
    if ascORdesc == "0":
        ascORdescBool = False
    elif ascORdesc == "1":
        ascORdescBool = True
    else:
        print("您的输入有误，请重新输入！")
        sort()
    mode = input("请选择排序方式（1按英语成绩排序；2按Python成绩排序；3按C语言成绩排序；0按总成绩排序）：")
    if mode == "1":
        student_new.sort(key=lambda x: x["english"], reverse=ascORdescBool)
    elif mode == "2":
        student_new.sort(key=lambda x: x["python"], reverse=ascORdescBool)
    elif mode == "3":
        student_new.sort(key=lambda x: x["c"], reverse=ascORdescBool)
    elif mode == "0":
        student_new.sort(key=lambda x: x["english"] + x["python"] + x["c"], reverse=ascORdescBool)
    else:
        print("您的输入有误，请重新输入！")
        sort()
    show_student(student_new)


def total():
    if os.path.exists(filename):
        with open(filename, 'r') as rfile:
            student_old = rfile.readlines()
            if student_old:
                print("一共有 %d 名学生！" % len(student_old))
            else:
                print("还没有录入学生信息！")
    else:
        print("暂未保存数据信息...")


def show():
    student_new = []
    if os.path.exists(filename):
        with open(filename, 'r') as rfile:
            student_old = rfile.readlines()
        for s_list in student_old:
            student_new.append(eval(s_list))
        if student_new:
            show_student(student_new)
    else:
        print("暂未保存数据信息...")


def show_student(studentList):
    if not studentList:
        print("(o@.@o) 无数据信息 (o@.@o) \n")
        return
    format_title = "{:^18}{:^0}\t{:^16}\t{:^8}\t{:^12}\t{:^14}"
    print(format_title.format("学号", "姓名", "英语成绩", "Python成绩", "C语言成绩", "总成绩"))
    format_data = "{:^6}{:^16}\t{:^81}\t{:^14}\t{:^12}\t{:^12}"
    for info in studentList:
        print(format_data.format(info.get("id"), info.get("name"), str(info.get("english")), str(info.get("python")),
                                 str(info.get("c")),
                                 str(info.get("english") + info.get("python") + info.get("c")).center(12)))


if __name__ == "__main__":
    main()
