from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {}

dispositivos = {}

class HelloWorld(Resource):
	def get(self):
		print(request.remote_addr)
		print(request.data)
		print(request.args)
		print(request.form)
		print(request.files)
		print(request.values)
		# if (request.remote_addr) not in dispositivos:
		# 	dispositivos[request.remote_addr] = {}

		# print(dispositivos)
		return {'hello': 'world'}

	def put(self):
		return {'hello': 'world'}

#class TodoSimple(Resource):
#	def get(self, todo_id):
#		return {todo_id: todos[todo_id]}
#
#	def put(self, todo_id):
#		todos[todo_id] = request.form['data']
#		return {todo_id: todos[todo_id]}

#api.add_resource(TodoSimple, '/<string:todo_id>')
api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)
	#app.run(debug=True)

