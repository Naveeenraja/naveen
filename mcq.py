from flask import Flask,render_template,request,redirect

import data.mcqutil as mcq_utils
file ="studreg.json"
file1 = "mcq.json"
app=Flask(__name__)

@app.route("/", methods=["POST" , "GET"])

def index():
    data = mcq_utils.read_json(file)
    return render_template("login.html", data= data["student registration"] )

@app.route("/login", methods= ["POST","GET"])
def login():
    data = mcq_utils.read_json(file)
    return render_template("mcq.html",data=data["student registration"])

@app.route("/register", methods=["POST" , "GET"])
def reg():
    msg="Your registration has been completed successfully !"
    data = mcq_utils.read_json(file)
    if request.method=="POST":
        length=len(data["student registration"])
        fname=request.form["firstname"]
        lname=request.form["lastname"]
        date_of_birth= request.form["dob"]
        gender= request.form["inlineRadioOptions"]
        email= request.form["email"]
        username= request.form["username"]
        password= request.form["password"]
        list_of_stud={
            "s_no" : length+1,
            "Firstname" : fname,
            "Lastname"  : lname,
            "DOB" : date_of_birth,
            "Gender" : gender,
            "Email" : email,
            "Username" : username,
            "Password" : password,
        }
        data["student registration"].append(list_of_stud)
        mcq_utils.write_json(file,data)
        msg="user " + username +" has been registered successfully!!!"
        data = mcq_utils.read_json(file)
        return render_template("login.html", data= data["student registration"], msg=msg)
    return render_template("mcq2.html", data=data["student registration"])
    
if __name__=="__main__":
    app.run(debug=True)   