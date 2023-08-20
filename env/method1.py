from flask import Flask, make_response, jsonify, request

app = Flask(__name__)

users = {
    "Alice": 1000,
    "Bob": 1500,
    "Charlie": 200,
    "David": 500,
    "Eve": 800
}

@app.route('/get_user/<name>', methods=['GET'])
def get_user(name):
    """
    gets a user with the given name

    Args:
        name (str): name of user

    Returns:
        response(object): user balance and response code on success, error message and error  code else
    """
    if name in users:
        user_data = {"name": name, "balance": users[name]}
        response = make_response(jsonify(user_data), 200)
        return response
    else:
        error_message = {"error": "User not found"}
        response = make_response(jsonify(error_message), 404)
        return response

@app.route('/delete_user/<name>', methods=['DELETE'])
def delete_user(name):
    """
    deletes user with name 

    Args:
        name (str): name of user

    Returns:
        response(object): success message and response code on success, error message and error  code else
    """
    if name in users:
        del users[name]
        response = make_response(jsonify({"message": f"User {name} deleted"}), 200)
        return response
    else:
        error_message = {"error": "User not found"}
        response = make_response(jsonify(error_message), 404)
        return response

@app.route('/add_user/<name>/<int:amount>', methods=['POST'])
def add_user(name, amount):
    """
    adds a new user and their balance

    Args:
        name (str): user name
        amount (int): balance

    Returns:
        response(object): success message and response code on success, error message and error  code else
    """
    if name in users:
        error_message = {"error": "User already exists"}
        response = make_response(jsonify(error_message), 409)
        return response
    else:
        users[name] = amount
        response = make_response(jsonify({"message": f"User {name} added with balance {amount}"}), 201)
        return response

@app.route('/update_user/<name>/<int:amount>', methods=['PUT'])
def update_user(name, amount):
    """
    updates an existing user 

    Args:
        name (str): _description_
        amount (int): _description_

    Returns:
        response(object): success message and response code on success, error message and error  code else
    """
    if name in users:
        users[name] = amount
        response = make_response(jsonify({"message": f"User {name} updated with balance {amount}"}), 200)
        return response
    else:
        error_message = {"error": "User not found"}
        response = make_response(jsonify(error_message), 404)
        return response

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

