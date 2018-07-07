from flask import Flask, jsonify
import os
from sqlalchemy import create_engine

app = Flask(__name__)

db = create_engine("postgres://rtakasu:TYgEuErh@soccer-database.conqzky6vos0.us-west-2.rds.amazonaws.com:5432/postgres")

@app.route('/')
def root():
	return "hello"

@app.route('/teams')
def teams():
	result = db.execute("select team_long_name from team order by team_long_name;")
	result_array = []
	for row in result:
		result_array.append(row['team_long_name'])
	return jsonify(result_array)

@app.route('/teams/search')
def teams_search():
	return "teamsearch"

if __name__ == '__main__':
	app.run()