import defnition
class mcq_question:
    def __init__(self, question,answers):
        self.questions = question
        self.answers = answers

name = input("enter your name: ") 
age = input("enter your age: ")       
   
question_prompt = defnition.read_json(r"D:\Education\python\naveen python.py\mcq_questions.json")  
test =[] 
for k,v in question_prompt.items(): 
    test.append(question(k,v))    
  
def ques(questions):
    score = 0
    for a in questions:
        ans=input(a.questions)
        if ans in a.answers:
            score +=1
        print ( "you got" + str(score) + "/" + str(len(questions))+ "correct")
        return score
    score=ques(test)
    
    test_data =   defnition.read_json(r"D:\Education\python\naveen python.py\mcq.json") 
    user_data = {
        "name": name,
        "age": age,
        "score": score
    }
    test_data["user"].append(user_data)
    defnition.write_json(r"D:\Education\python\naveen python.py\mcq.json",test_data)