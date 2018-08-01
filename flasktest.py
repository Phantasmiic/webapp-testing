from flask import Flask, render_template, request, url_for, redirect, jsonify
import json
app = Flask(__name__)


data = [[1,2,3],[4,5,6]]


		
@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == "POST":
		data = request.get_json()
		print('this is data')
		print(data)	
		if data != None:
			print('adadad')
			
			writeData(json.dumps(data))
			return render_template("dropdown.html", car_brand = data)
	writeData('failed')
	return render_template("dropdown.html")

		

def writeData(data):
	with open('data/machine1.txt', 'w') as dataRead:
		dataRead.write(data)
	pass
		
if __name__ == '__main__':
    app.run(debug=True)
	
