orginal_string = ["python", "exercises", "practice", "solution", "exercises"]
user_input =int(input("which element you want to remove: "))

if orginal_string.count(orginal_string[user_input])==1:
    print("not dublicate found")
    
else :
    print("dublicate found")
    orginal_string.pop(user_input)
    list_of_string = orginal_string.copy()
    print("list of string =" , list_of_string)
    
       
    
