import json
def read_json(file):
    f= open(file,"r")
    data = json.load(f)
    f.close()
    return data

def write_json(file, data):
    fw= open(file, "w")
    data_to_be_written = json.dumps(data, indent=3, sort_keys=True)
    fw.write(data_to_be_written)
    fw.close()

# def age_calculation(age):
#     calculate_age = (2022 - age[0]) , (12 - age[1]) , (31 - age[2])
#     return calculate_age

# orginal_age = []

# orginal_age.append(int(input("enter a year: ")))
# orginal_age.append(int(input("enter a month: ")))
# orginal_age.append(int(input("enter a days: ")))

# real_age =age_calculation(orginal_age)
# print(f"your current age is {real_age[0]} years and {real_age[1]} months and {real_age[2]} days")
