from flask import*
import os
import shutil
import webbrowser

def rf(a):
	return open(a,"r").read()

def store_data(a,b):
	return "<script>localStorage.setItem('"+a+"','"+b+"');</script>"

def alert(a,b):
	return rf('alert.html').replace("a9341",a) + rf(b)

app = Flask(__name__, static_folder="a")

@app.route("/")
def a():
	return rf("index.html").replace("content","")

@app.route("/login", methods=["GET","POST"])
def a_1():
	if (request.method == "GET"):
		return rf("login.html")
	else:
		f1=[request.form["username"],request.form["password"]]
		if (f1[0] in os.listdir("acc")):
			if (rf("acc/"+f1[0]+"/pass") == f1[1]):
				return rf("index-m.html") + store_data("username",f1[0])
			else:
				return alert("Wrong password","login.html")
		else:
			return alert("Account does not exist","login.html")

@app.route("/create", methods=["GET","POST"])
def a_2():
	if (request.method == "GET"):
		return rf("create.html")
	else:
		f1=[request.form["username"],request.form["password"]]
		if (f1[0] in os.listdir("acc")):
			return alert("Account with this username already exist!!","create.html")
		else:
			os.mkdir("acc/"+f1[0])
			open("acc/"+f1[0]+"/pass","a").write(f1[1])
			return alert("Account created","index-m.html") + store_data("username",f1[0])

@app.route("/delete", methods=["GET","POST"])
def a_3():
	if (request.method == "GET"):
		return rf("delete.html")
	else:
		f1=[request.form["username"],request.form["password"]]
		if (f1[0] in os.listdir("acc")):
			shutil.rmtree("acc/"+f1[0])
			return rf("goodbye.html")
		else:
			return alert("Account does not exist!!","create.html")


@app.route("/newpassword", methods=["GET","POST"])
def a_4():
	if (request.method == "GET"):
		return rf("newpassword.html")
	else:
		f1=[request.form["username"],request.form["password"],request.form["newpassword"]]
		if (f1[0] in os.listdir("acc")):
			if (rf("acc/"+f1[0]+"/pass") == f1[1]):
				open("acc/"+f1[0]+"/pass","w").write(f1[2])
				return alert("Your password has been changed!!","index.html") + store_data("username",f1[0])
			else:
				return alert("Wrong password","newpassword.html")
		else:
			return alert("Account does not exist","newpassword.html")

@app.route("/newusername", methods=["GET","POST"])
def a_5():
	if (request.method == "GET"):
		return rf("newusername.html")
	else:
		f1=[request.form["username"],request.form["password"],request.form["newusername"]]
		if (f1[0] in os.listdir("acc")):
			if (rf("acc/"+f1[0]+"/pass") == f1[1]):
				if (f1[2] in os.listdir("acc")):
					return alert("Account with this username already exist, try another username!!","newusername.html")
				else:
					os.rename("acc/"+f1[1],"acc/"+f1[2])
					return alert("Your username changed successfully","newusername.html") + store_data("username",f1[2])
			else:
				return alert("Your password is wrong","newusername.html")
		else:
			return alert("Account does not exist","newusername.html")

@app.errorhandler(404)
def a_6(a):
	return rf("404.html")

#webbrowser.open("http://127.0.0.1:5000/")

app.run()