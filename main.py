import json

def read_from_file():
    try:
        file = open("studentdb.json", "r")
        file_content_as_text = file.read()
        students = json.loads(file_content_as_text)
        file.close()
        return students
    except :
        return []

def write_to_file(student):
    file = open("studentdb.json", "w+")
    json_text = json.dumps(student,indent=4)
    file.writelines(json_text)
    file.close()

def add():
    add_student = dict()
    add_student['name'] = Capital_Format((str(input("Enter Your Name :  "))).strip())

    add_student['id']= (str(input("Enter Your ID :  "))).strip()
    f = bool(checkidnum(add_student['id']))
    if not f:
        print(end="")
    else:
        while True:
            add_student['id'] = (str(input("Wrong Id ! Enter ID Again ! :  "))).strip()
            f = bool(checkidnum(add_student['id']))
            if not f:
                break
    add_student['gmail'] = (str(input("Enter Your Gmail ID :  "))).strip()
    add_student['gender'] = (str(input("Enter Your Gender :  "))).strip()




    list = []

    p=int(input("How Many Course You Want Register ? "))
    for i in range(p):
        p=input("Enter Course Code :  ")
        if p in list:
            print("Wrong course code!")
            p = input("Enter Course Code Again :  ")
            while True:
                if p in list:
                    print("Wrong course code!")
                    p = input("Enter Course Code Again")
                else:
                    break
        list.append(p)
    add_student['section'] = input("Enter Your Section Name :  ")


    add_student['course_list'] = list

    add_student['registration_status'] = "Pending"

    students = read_from_file()

    students.append(add_student)

    write_to_file(students)

    print("\n***** --------------                Successfully Added!      ---------------    *****\n")


def checkidnum(id):
    s = read_from_file()
    f_id= 0
    for student in s:
        if student.get("id") == id:
            return 1
    return f_id

def search( id ):

    s= read_from_file()
    foundid= False
    for student in s:


        if student.get("id") == id:
            print()
            print("Name : " + student.get("name"))
            print("ID : ", student.get("id"))
            print("Gmail Id : ", student.get("gmail"))
            print("Gender: ", student.get("gender"))
            print("Course List : ")
            j = 1
            for i in student.get("course_list"):
                print("\t", j, end="." + " " + i + "\n")
                j += 1
            print("Section : ", student.get("section"))
            print("Registration Status : ", student.get("registration_status"))
            return True

    return foundid

def update():

    u= (str(input("Enter ID :  "))).strip()
    s = read_from_file()
    new= []
    f = False
    for student in s:

        if student.get("id") == u:
            f = True
            print("Name : " + student.get("name"))
            print("ID : ", student.get("id"))
            print("Gmail Id : ", student.get("gmail"))
            print("Gender: ", student.get("gender"))
            print("Course List : ")
            j = 1
            for i in student.get("course_list"):
                print("\t", j, end="." + " " + i + "\n")
                j += 1
            print("Section : ", student.get("section"))
            print("Registration Status : ", student.get("registration_status"))



            print("Select your option : ")
            print("1. Pending Status")
            print("2. Partially Complete Status")
            print("3. Complete Status")
            print("4. Not now")
            option = int(input())
            if  option  == 1:
                student['registration_status']="Pending"
                print(" Successfully !")
            elif  option  == 2 :
                student['registration_status'] = "Partially Complete"
                print(" Successfully !")
            elif  option == 3 :
                student['registration_status'] = "Complete"
                print("Successfully !")
            elif  option == 4:
                print("Not Changing")
            else:
                print("Wrong Info !")
            new.append(student)
        else:
            new.append(student)
    if not f :
        print(" Not Found !\n")
    else:
        write_to_file(new)

def delete():
    s = read_from_file()
    new= []
    statement=int(input("1.Delete All Account \n2.Delete One Account\n3.Don't want delete\n"))
    if statement==1:
        sure=int(input("1.Are you sure delete all record\n2.If not\n"))
        if sure==1:
            write_to_file(new)
            print(">>>>>>*            All Student Data Delete Successfully         *<<<<<<\n")
            return
        else:
            delete()

    elif statement == 2:
        id = (str(input("Enter ID for Delete:  ")).strip())
        check = False
        for student in s:
            if id == student.get("id"):
                check = True
                pass
            else:
                new.append(student)
        write_to_file(new)
        if not check:
            print("\n>>>>>>                Student Not Found !                 <<<<<<\n")
        else:
            print(">>>>>>*               Student Delete Successfully         *<<<<<<\n")
    elif statement == 3:
        return()

def view_record():
    s = read_from_file()
    for student in s:
        print("Name : "+student.get("name"))
        print("ID : ",student.get("id"))
        print("Gmail Id : ", student.get("gmail"))
        print("Gender: ", student.get("gender"))
        print(student.get("name")," Course List : ")
        p=1
        for i in student.get("course_list"):
            print("\t",p,end="."+" "+i+"\n")
            p+=1
        print("Section : ", student.get("section"))
        print( "Registration Status : ",student.get("registration_status"))
        print()

def countstudent():
    p_s=0
    c_s=0
    p_c_s=0
    s = read_from_file()
    for student in s:
        if student.get("registration_status")=="Pending":
            p_s += 1
        elif student.get("registration_status")=="Partially Complete":
            p_c_s += 1
        elif student.get("registration_status")=="Complete":
            c_s += 1
    print(" Total Student :  ",p_s+p_c_s+c_s)
    print(" Pending Status Student :  ",p_s)
    print(" Partially Complete Status Student : ",p_c_s)
    print(" Complete Status Student :  ",c_s,"\n")

def Capital_Format(name):

    return ' '.join(map(lambda name: name[:-1] + name[-1],name.title().split()))

while True:
    print(">>>>>>>>>>>>>>>>>>>>>>>>>*****<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print("***               1. Create New Registration                ***")
    print("***               2. Search Student By ID                   ***")
    print("***               3. Update Student Registration by Status  ***")
    print("***               4. Delete Student Record                  ***")
    print("***               5. View Student  Record                   ***")
    print("***               6. Teacher Account                        ***")
    print("***               7. Exit                                   ***")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>*****<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")
    select = int(input("********* Select Any Option ***********\n"))

    if select == 1:
        add()

    elif select ==2:
        search_id = (str(input("Enter Search  ID :  "))).strip()
        found = search( search_id )
        if not found:

            print(">>>>>>                Student Not Found !                 <<<<<<")


    elif select== 3:
        update()

    elif select== 4:
        delete()

    elif select== 5:
        view_record()

    elif select == 6:
        countstudent()

    elif select== 7:
        exit()
