from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)


data = [[1,2,3],[4,5,6]]

@app.route('/')
@app.route('/index')
def index():
    return render_template("dropdown.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == "POST":
		function = request.form.get("function", None)
		if function!=None:
			writeData(function)
			
			# if function == 'StickIn':
			# elif function == 'StickOut':
			# elif function == 'BoomUp':
			# elif function == 'BoomDown':
			
			
			return render_template("dropdown.html", function=function)
	#writeData("Nothing yet")
	#return render_template("dropdown.html")
	return render_template("dadadada")



def writeData(data):
	#with open('data/machine1.txt', 'w') as dataRead:
	#	dataRead.write(data)
	pass
		
if __name__ == '__main__':
    app.run(debug=True)