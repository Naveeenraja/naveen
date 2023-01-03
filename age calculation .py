def age_calculation(age):
    calculate_age = (2022 - age[0]) , (12 - age[1]) , (31 - age[2]) , (24 - age[3])
    return calculate_age

orginal_age = []

orginal_age.append(int(input("enter a year: ")))
orginal_age.append(int(input("enter a month: ")))
orginal_age.append(int(input("enter a days: ")))
orginal_age.append(float(input("enter a hour: ")))
real_age =age_calculation(orginal_age)
print(f"your current age is {real_age[0]} years and {real_age[1]} months and {real_age[2]} days and {real_age[3]}hours")

# def letter(vow):
#     vowels = ["a" , "e" , "i" , "o" , "u"]
#     if vow in vowels:
#         print("vow in vowles")
#     else:
#         print("vow in not a vowel")
#letter("i")

# def sides(a,b):
#     if a==b:
#         print("the given sides are square")
#     else:
#         print("the given sides are not square")  
# sides(2,2)              

# def sides(a,b):
#     if a==b:
#         print("the given sides are square")
#     if a!=b:
#         print("the given sides are rectangle")
        
# sides(a= input("enter a value 1: ") , b= input("enter a value 2: "))   
# result = sides("a","b")     


def list(value):
    sample_list = ["abc" , "xyz" , "aba" , "1221"] 
    if len(sample_list[0],len(sample_list[1],len(sample_list[2]),len(sample_list[3])))==2:
        print("good")            
    else:
        print("bad")  
list          