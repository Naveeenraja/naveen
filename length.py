sample_list= ["abc", "xy","a","aba", "1221"]
# user_input = int(input("enter a value: "))


# if (len(sample_list[user_input])) >=2 and (sample_list[user_input][0]== sample_list[user_input][-1]):
#     print("both conditions are satisfied")
# else:
#     print("the string length more than 2 but first and last letter is not same")    
    
count = 0

for index in range(len(sample_list)):
    if (len(sample_list[index])>=2):
        if sample_list[index][0]==sample_list[index][-1]:
         print("both the condition are satisfied")
         count +=1
        else:
         print("the string lenghth is 2 or more than 2 but first letter and last letter are not same")
    else:
      print("both the conditions are not satisfied")    
      
print(str(count))              
          

    
    