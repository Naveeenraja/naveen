# orginal_nested_list = [
# [1,2,3],
# [2,4,5],
# [1,1,1]    
# ]
# user_input = int(input("enter a value: "))
# def remove_coloum(nums,user_input):
#     for i in nums:
#         del i[user_input]
#     return nums
# print(remove_coloum(orginal_nested_list,user_input))
    
        
    
# # user_input = int(input("enter a base value: "))
# # listt = []
# # for i in range (1,user_input+1):
# #     line = ""
# #     for j in range(i,user_input+1) : 
# #         line = "*" + line
# #     for m in range(i):
# #         line = " "+line
      
# #     listt.append(line)
# # listt.reverse()
# # for k in listt:
# #     print(k) 
# # listt.reverse()
# # listt.remove(listt[0]) 
# # for k in listt:
# #     print(k)   
   
# #triangle my style
user_input = int(input("enter a base value: "))
listt = []
space = 0
while user_input>0:
    for i in range(1,user_input+1):  
        line = ""
    for j in range (i):
            line = "*" + line
    for m in range(space):
            line= " "+line
    listt.append(line)        
    user_input-=2
    space+=1    
listt.reverse()
for k in listt:
    print(k)
listt.reverse()
listt.remove(listt[0]) 
for k in listt:
    print(k) 

  
# pyramid my style
# user_input = int(input("enter a base value: "))
# lst = []
# for i in range(1, user_input+1):
#     line = " "
#     for j in range(i,user_input+1):
#         line = line + "* "
#     for m in range(i):
#             line = " " + line
           
#     lst.append(line)
# lst.reverse()

# for k in lst:
#     print(k) 
# lst.reverse()
# lst.remove(lst[0])  
# for k in lst:
    # print(k)       



# rows = int(input("enter a row value: "))
# col = int(input("enter a col value: "))

# for i in range(rows):
#     for j in range(col):
#       if i==0 or i ==(rows-1) or j==0 or j ==(col - 1) :
#            print("*", end=" ")
        
#       else: 
#         print("  ", end="") 
#     print()    

orginal_nested_list = [
[1,2,3],
[2,4,5],
[1,1,1]    
]
removing_colu = int(input("enter a user input: "))
def removing_col(numers,removing_colu):
    for i in numers:
        del i [removing_colu]
    return numers

print(removing_col(orginal_nested_list,removing_colu))


        
    
        