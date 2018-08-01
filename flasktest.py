from flask import Flask, render_template, request, url_for, redirect, jsonify
import json
app = Flask(__name__)


data = {"StickIn": 100,
		"StickOut": 200,
		"BoomOut":300,
		"BoomUp":400}


		
@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == "POST":
		functionality = request.get_json()
		# print('this is data')
		# print(data)	
		if functionality != None:
			#processData(data)
			writeData(json.dumps(functionality))
			return render_template("dropdown.html", par_dict = 'this is retarded')

	writeData('failed')
	return render_template("dropdown.html", par_dict = 'adadadad')

@app.route('/processData/<data>')
def processData(data):
	functionality = data
	if functionality != None:
		return jsonify(data)
	return jsonify('failed')

def writeData(data):
	with open('data/machine1.txt', 'w') as dataRead:
		dataRead.write(data)
	pass
		
if __name__ == '__main__':
    app.run(debug=True)
	
