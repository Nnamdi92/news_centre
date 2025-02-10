from flask import Flask, jsonify, request
from database.connect import create_server_connection
from routes.get_all_news import get_all_news

app = Flask(__name__)
    
connection = create_server_connection("bt-newsapi-db-prod.c3ka2iwk2b6o.us-east-1.rds.amazonaws.com", "root", "Havard1992")


@app.route("/", methods=["GET"])
def home():
    return jsonify(message="Welcome to our News API")

@app.route("/allnews", methods=["GET"])
def get_news():
    data=get_all_news(connection)
    return jsonify(message=data)

#This route/endpoint is to retrieve all news from the database

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
