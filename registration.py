import defnition
from collections import OrderedDict


    
   
    





def registration():
    data = defnition.read_json(r"D:\Education\python\naveen python.py\myfile.json") 
    lenghth = len(data["students"]) + 461370
    
    user_data = {
        "name": input("enter your name: "),
        "age" :input("enter your age: "),
        "qualification" : input("enter your qualifications: "),
        "experience" : input("enter your experience: "),
        "iD" : lenghth +1
}
    
    data["students"].append(user_data)  
    defnition.write_json(r"D:\Education\python\naveen python.py\myfile.json", data) 
    
def update_user():
    data= defnition.read_json(r"D:\Education\python\naveen python.py\myfile.json")
    for i in data["students"]:
        print("ID: " + str(i["iD"]) + " Name: "+ i["name"])
    user_present = False 
    user = input("enter the user you want to update: ") 
    print("do you want to update\n1. Name\n2. Age\n3. Qualification\n4. Experience\n5. Update all details") 
    choice = input("enter your choice(1,2,3,4,5): ")
    for i in data["students"]:   
        user_present= True
        if i["name"]==user:
            if choice=="1":
                user_2 = input("enter your update input:  ")
                del i["name"]
                i["name"]=user_2
                print(f" {user_2} has been update successfully!!!!!!!")
            elif choice=="2":
                user_2 = input("enter your update input:  ")
                del i["age"]
                i["age"]=user_2 
                print(f" {user_2} has been update successfully!!!!!!!") 
            elif choice=="3":
                user_2 = input("enter your update input:  ")
                del i["qualification"]
                i["qualification"]=user_2   
                print(f" {user_2} has been update successfully!!!!!!!")
            elif choice=="4":
                user_2 = input("enter your update input:  ")
                del i["experience"]
                i["experience"]=user_2 
                print(f" {user_2} has been update successfully!!!!!!!")  
            else:
                registration()
                print("\t\tall details has been update successfully!!!!!!!")
                break
            defnition.write_json(r"D:\Education\python\naveen python.py\myfile.json",data) 
            user_present= False
            break             
        if not user_present:
            print(f" {user} not found in data base.....please enter valid input!!!!!")   
        defnition.write_json(r"D:\Education\python\naveen python.py\myfile.json",data)     
       
        
def delete_user():
    data = defnition.read_json(r"D:\Education\python\naveen python.py\myfile.json")
    for i in data["students"]:
        print("ID: " + str(i["iD"]) + " Name: "+ i["name"])
    user_present = True
    user = input("enter the user you want to delete: ") 
    print("Do you want to delete\n1. Name\n2. Age\n3. Qualification\n4. Experience\n5. All details")
    choice= input("enter your choice(1,2,3,4,5): ")
    for i in data["students"]:
        user_present = False
        if i["name"]==user:
            if choice=="1":
                del i["name"]
                i["name"] = ""
                print(f" {user} has been removed successfully!!!!!!!")
               
            elif choice=="2":
                del i["age"]  
                i["age"]= ""
                print(f" {user}'s age has been removed successfully!!!!!!!")
                
            elif choice =="3":
                del i["qualification"]
                i["qualification"]  = ""  
                print(f" {user}'s qualification has been removed successfully!!!!!!!")
                
            elif choice=="4":
                del i["experience"]
                i["experience"]="" 
                print(f"{user}'s experiennce has been removed successfully!!!!!!!")
                
            elif choice==5:
                data["students"].remove(i) 
                print(f" {user}'s all details has been removed successfully!!!!!!!")
                
            else:
                print("you are enter invalid input!!!!!")
                break
                
    defnition.write_json(r"D:\Education\python\naveen python.py\myfile.json",data)  
                      
    if  user_present:
            print(f" {user} not found in data base...please enter proper value!!!!")
    defnition.write_json(r"D:\Education\python\naveen python.py\myfile.json",data) 
        


print("\t\t\twelcome to the student registration!!!!!")
while True:
    print("\t\t\tyou can do the following operations\n1. registration\n2. update user\n3. delete user")
    choice = input("enter your choice(1,2,3): ")
    if choice not in "1,2,3":
        print("you entered invalid input...!!!!!")
        print("please provide valid input.....!!!!")
        continue
    if choice=="1":
        registration()
        print("\t\tsucessfully you complete your registration process!!!!!") 
        
    elif choice=="2":
        update_user()
    else:
        delete_user()   
        
         
    print("1. press A for continue\n2. press B for back home")
    is_continue= input("do you want to continue or back for home: ") 
    if is_continue=="A":
        continue
    elif is_continue=="B":
        break
    else:
        break   