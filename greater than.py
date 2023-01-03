# a= float(input("enter a value: "))

# if a<100:
#     print("the given num lesser than 100")

# elif a<1000:
#     print("the given value lesser than 1000")

# elif a<2000:
#     print("the given value lesser than 2000")

# else:
#     print("you enter invalid num")


# a = open(r"D:\Education\python\pytho.txt", )

# # a.write("""\nennatha solla
# # solla onnum illa
# # petru eduthu poona""")
# # a.close()
# print(a.readable(-1))

try:
    num = int(input("enter a num: "))
    num_2 = int(input("enter a num: "))
    print(num/num_2)
    
except ZeroDivisionError:
    print("division by zero is not possible")
    print("please enter correct input values") 
    num = int(input("enter a num: "))
    num_2 = int(input("enter a num: "))
    print(num/num_2)
    
except ValueError:
    print("invalid input")  
    print("please enter correct input values") 
    num = int(input("enter a num: "))
    num_2 = int(input("enter a num: "))
    print(num/num_2)  
       
   