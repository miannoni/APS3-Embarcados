from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {}

dispositivos = {}

class recebe(Resource):
	def get(self):
		global analogico, digital
		# analogico = request.args.get("Analogico")
		digital = request.args.get("Digital")
		digital = int(digital)
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
	
   '''.format(digital)

# @app.route('/python')

# def hello_python():
#    return 'Hello Python'
if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)
	#app.run(debug=True)

