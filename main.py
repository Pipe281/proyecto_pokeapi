from flask import Flask, jsonify, request
#from test import 
app = Flask(__name__)

from prueba import users_list

@app.route('/')
def hello():
    return jsonify({"message": "Hello!"})


@app.route("/user")
def getProducts():
    return users_list


if __name__ == '__main__':
    app.run(debug=True, port=4000)




