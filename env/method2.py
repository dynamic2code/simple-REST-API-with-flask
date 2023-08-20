from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

users = {
    "Alice": 1000,
    "Bob": 1500,
    "Charlie": 200,
    "David": 500,
    "Eve": 800
}

class GetUser(Resource):
    def get(self, name):
        if name in users:
            user_data = {"name": name, "balance": users[name]}
            return user_data, 200
        else:
            return {"error": "User not found"}, 404
        
class DeleteUser(Resource):
    def delete(self, name):
        if name in users:
            del users[name]
            user_data = {"message": f"User {name} deleted"}
            return user_data, 200
        else:
            return {"error": "User not found"}, 404
        
class AddUser(Resource):
    def post(self, name, amount):
        if name in users:
            return {"error": "User already exists"}, 409
        else:
            users[name] = amount
            response = {"message": f"User {name} added with balance {amount}"}
            return response, 201

class UpdateUser(Resource):
    def put(self, name, amount):
        if name in users:
            users[name] = amount
            response = {"message": f"User {name} updated with balance {amount}"}
            return response,200
        else:
            return {"error": "User not found"}, 404

api.add_resource(GetUser, '/get_user/<string:name>')
api.add_resource(DeleteUser, '/delete_user/<string:name>')
api.add_resource(AddUser, '/add_user/<name>/<int:amount>')
api.add_resource(UpdateUser,'/update_user/<name>/<int:amount>')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
