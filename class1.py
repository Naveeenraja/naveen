class Student:
    def __init__(self, name,veg_dish,non_veg_dish):
        self.name = name
        self.veg_dish = veg_dish
        self.non_veg_dish = non_veg_dish
        
    def place_order(self):
        if self.veg_dish:
            print(f" {self.name} has been cooking {self.veg_dish}")  
            print(input("waiting min: "))  
            print("your order is ready")
        elif self.non_veg_dish:
            print(f" {self.name} has been cooking {self.non_veg_dish}")  
            print(input("waiting min: "))  
            print("your order is ready")
                
    # def check_distinct(self):
    #     if self.gpa>8.5:
    #         print(f"the student {self.name} passed with distinction")
    #     else:
    #         print(f"the student {self.name} passed with first class")        
    