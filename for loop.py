# a = ["sakthi", "naveen", "raja", "pranav"]
# for name in a:
#     print(len(a))
# for index in range(len(a)):
#     if index==0:
#         print("he is my best friend")
#         print(a[index])

# # for index in range(1,5):
#     # print(index)

# alphabet = [
# ["a","b","c","d","e"],
# ["f","g","h","i","j"],
# ["k","l","m","n","o"],
# ["p","q","r","s","t"],
# ["u","v","w","x","y","z"],
# ]
# for row in alphabet:
#     for col in row:
#         print(row)




# def make_triangle(size):
#     list = []
#     a = size
#     while a>0:
#         line = ""
#         for b in range(a):
#             line = line+"*"
#         a-=1
#         list.append(line)
#     list.reverse()
#     for c in list:
#         print(c)


# size_of_triangle = int(input("enter base size: "))
# make_triangle(size_of_triangle)

# def make_a_triangle(size):
#     x = size
#     while x>0:
#         line = ""
#         for y in range(x):
#             line=line+"*"
#         x = x - 1
#         print(line)
# size_of_the_triangle = int(input("enter a base value: "))
# make_a_triangle(size_of_the_triangle)

# rows= int(input("enter a num of rows: "))

# for i in range(rows):
#     for j in range(i + 1):
#         print(j + 1 , end=" ")
#     print("\n")

# for i in range(rows,0,-1):
#     for j in range(0,i):
#         print("*" , end=" ")
#     print("\n")

#straight small one side triangle
user_input = int(input("enter a base value: "))
listt = []
# for i in range(1,user_input + 1):
#     line = ""
#     for j in range(i):
#         line = line + "*"
#     print(line)


#reverse small one side triangle
# for i in range(1,user_input + 1):
#     line = ""
#     for j in range (i):
#         line = line + "*"
#     listt.append(line)
# listt.reverse()
# for k in listt:
#   print(k)

#right side pyramid
# for i in range(1,user_input+1):
#     line = ""
#     for j in range(i):
#         line = line + "*"
#     listt.append(line)
# for k in listt:
#     print(k)
# listt.reverse()
# listt.remove(listt[0])

# for k in listt:
#     print(k)

#right side arrow
# for i in range(1,user_input+ 1):
#     line = ""
#     for j in range(i):
#         line = "*" + line
#     for m in range(i):
#          line = " "+ line

#     listt.append(line)
# for k in listt:
#     print(k)
# listt.reverse()
# listt.remove(listt[0])

# for k in listt:
#     print(k)

#left side pyramid
# for i in range(1,user_input+ 1):
#     line = ""
#     for j in range(i,user_input+ 1 ):
#         line = "*" + line
#     for m in range(i):
#          line = " "+ line

#     listt.append(line)
# listt.reverse()


# for k in listt:
#     print(k)

# listt.reverse()
# listt.remove(listt[0])

# for k in listt:
#     print(k)

#pyramid
# m = 0
# while user_input>0:
#     line = ""
#     for j in range(user_input):
#         line = "*" + line
#     for k in range(m):
#         line = " " + line
#     listt.append(line)
#     user_input-=2
#     m+=1
# listt.reverse()
# for j in listt:
#     print(j)
# listt.reverse()
# for j in listt:
#     print(j)

# square
# for i in range (1,user_input+1):
#     for j in range(1,user_input+1):
#         print("*", end=" ")
#     print()

#rectangle
# for i in range (1,user_input-1):
#     for j in range(1,user_input+1):
#         print("*", end=" ")
#     print()

row = int(input("enter a row value: "))
coloum = int(input("enter a coloum value: "))

for i in range (row):
    for j in range(coloum):
        if i==0 or i==(row -1) or j==0 or j ==(coloum-1):
         print("*", end="  ")
        else:
            print("   ", end="")
    print()