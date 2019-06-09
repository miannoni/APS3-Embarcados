from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {}

dispositivos = {}

class recebe(Resource):
	def get(self):
		global analogico, digital
		if (request.args.get("Analogico")):
			analogico = request.args.get("Analogico")
			analogico = int(analogico)
		else:
			analogico = 0
		if (request.args.get("Digital")):
			digital = request.args.get("Digital")
			digital = int(digital)
		else:
			digital = 0

			
		# print(request.time)
		return "recebido"

# class GG(Resource):
# 	def get(self):
# 		string = "<h1>{0}<h1>".format(digital)
# 		return string

# 	def post(self):
# 		print(request.data)
# 		return "oizinho"



api.add_resource(recebe, '/')
# api.add_resource(GG, '/Recebe')

@app.route('/show')

def show():
   return '''
	
   <h1> {0} <h1>
   <h1> {1} <h1>
	
   '''.format(analogico, digital)

# @app.route('/python')

# def hello_python():
#    return 'Hello Python'
if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)
	#app.run(debug=True)

