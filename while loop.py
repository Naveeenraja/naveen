print("\t\twelcome to the python riddle")
print("\ntoday riddle: im tall when im young, and im short when im old, who am i?")

ans = "candle"

choice = 1

def check_ans(ans):
    if ans == "candle":
        print("GLORY!!!!")
        print("you won!!!!!!")
        return True
    else:
        return False
    
while choice <=4:
    if choice==1:
        print("this is your first chance!!!!")
    elif choice==2:
        print("this is your second chance!!!!")  
    elif choice==3:
        print("this is your third chance!!!!")
    else:
        print("this is your last chance!!!!")
        print("your clue is : this element using for houses after power cut") 

    user_input = input("enter your choice: ") 
    if check_ans(user_input) :
        break
    if choice==4:
     print("you loose!!!!!")
     print("better luck next time") 
    choice +=1   
        
                     
    
    
    