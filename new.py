@app.route("/forgot" , methods=["POST" , "GET"])  
def forgot():
    return render_template("forgot.html")

@app.route("/sentotp" , methods=["POST" , "GET"])
def otp():
    data = mcq_utils.read_json(file)
    num="0105"
    mes=""
    if request.method=="POST":
        email=request.form["email"]
        mes="your email id is incorrect / did not register / dont recognize"
        for i in data["student registration"] : 
            if i["Email"]==email:
                return render_template("otp.html", num=num)
    return render_template("forgot.html" , mes=mes)
