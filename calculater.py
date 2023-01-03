import naveen

print("\t\t\twelcome to the python calculator!!!!")
print("you can perform the following operations: \n01. additon\n02. substraction\n03. multipication\n04. division\n05. simple intrest\n06. compound intrest\n07. fahrenhit to celsius\n08. celsius to fahrenhit\n09. fahrenhit to kelvin\n10. celsius to kelvin\n11. square root\n12. cubic root\n13. volume of square\n14. volume of rectangle\n15. volume of circle\n16. volume of right angle triangle\n17. volume of rhombus\n18. volume of parallelogra\n19. volume of trapezium\n20. perimeter of square\n21. perimeter of rectangle\n22. perimeter of circle\n23. perimeter of rhombus\n24. perimeter of parallelogra\n25. perimeter of trapezium\n26. volume of cube\n27. total surface area of cube\n28. volume of cuboid\n29. total surface area of cuboid\n30. volume of sphere\n31. curved surface area of sphere\n32. total surface area of sphere")
choice = int(input("enter the choice of operation[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]: "))
oper = [" addition", " substraction", " multiplication", " division", " si calculation", " ci calculation" , " fahrenhit to celsius" , " celsius to fahrenhit" , " fahrenhit to kelvin", " celsius to kelvin", " square root " , " cubic root ", "volume of square", "volume of rectangle", "volume of circle", "volume of right angle triangle", "volume of parallelogra", "volume of trapezium", "perimeter of square", "perimeter of rectangle", "perimeter of circle", "perimeter of rhombus", "perimeter of parallelogra", "perimeter of trapezium", "volume of cube", "total surface area of cube", "volume of cuboid", "total surface area of cuboid", "volume of sphere", "curved surface area of sphere", "total surface area of sphere"]
print("proceeding with operation" + oper[choice-1])


if choice==5:
    principal_amount = float(input("enter a amount: "))
    intrest = float(input("enter a intrest: "))
    years = float(input("enter a years: "))
    amt,si = naveen.si(principal_amount,years,intrest)
    print("simple intrest amount is: " + str(si))
    print("total amount to be repaid: " + str(amt))
    
elif choice==6:
        principal_amount = float(input("enter a amount: "))
        intrest = float(input("enter a intrest: "))
        years = float(input("enter a years: "))
        amt,ci = naveen.ci(principal_amount , years, intrest)
        print("coumpound intrest amount is: " + str(ci))
        print("total amount to be repaid: " + str(amt))

elif choice==7:
    fahrenhit_value = float(input("enter a fahrenhit value: "))
    cel = naveen.celsius_farhrenhit (fahrenhit_value)
    print(str(cel)+"C") 
    
elif choice==8:
    celsius_value = float(input("enter a celsius value: "))
    fahrenhit = naveen.celsius_farhrenhit(celsius_value)   
    print(str(fahrenhit)+"F") 
    
elif choice==9:
    fahrenhit  = float(input("enter a fahrenhit value: "))
    kelvin = naveen.fahrenhit_to_kelvin(fahrenhit) 
    print(str(kelvin)+"K")
    
elif choice==10:
    celsius = float(input("enter a celsius value: "))   
    kelvin = naveen.celsius_to_kelvin(celsius)      
    print(str(kelvin)+"K")
        
elif choice ==11:
    a = float(input("enter a value: "))
    square_root = naveen.square_root(a) 
    print(square_root)   
    
elif choice==12:
    a = float(input("enter a value: "))
    cubic_root = naveen.cubic_root(a)  
    print(cubic_root)    
    
          
else:
    num_1 = float(input("enter a first num: "))
    num_2 = float(input("enter a second num: "))
    
    if choice==1:
        result = naveen.add(num_1, num_2)
        print("the result of given value is: " + str(result))
       
    elif choice==2:
        result = naveen.sub(num_1 , num_2) 
        print("the result of the given value is: " + str(result))
         
    elif choice==3:
        result = naveen.mul(num_1 , num_2) 
        print("the result of the given value is: " + str(result)) 
        
    elif choice==4:
        result = naveen.div(num_1 , num_2) 
        print("the result of the given value is: " + str(result))  
        
    else:
        print("you have entered a invalid num") 
                          
        
    
    
    