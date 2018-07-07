from flask import Flask, jsonify, redirect, url_for
import os
from sqlalchemy import create_engine

app = Flask(__name__)

db = create_engine("postgres://rtakasu:TYgEuErh@soccer-database.conqzky6vos0.us-west-2.rds.amazonaws.com:5432/postgres")

@app.route('/')
def root():
	return "hello"

@app.route('/players/')
def players_page0():
	result = db.execute("SELECT full_name FROM players ORDER BY full_name LIMIT 100;")
	result_array = []
	for row in result:
		result_array.append(row['full_name'])
	return jsonify(result_array)

@app.route('/players/page=<page_no>')
def players_page(page_no):
	result = db.execute("SELECT full_name FROM players ORDER BY full_name LIMIT 100 OFFSET " + str(int(page_no)*100) + " ;")
	result_array = []
	for row in result:
		result_array.append(row['full_name'])
	return jsonify(result_array)

@app.route('/players/search/')
def players_search():
	return "players search"

@app.route('/teams')
def teams():
	# return all clubs
	return "clubs"

@app.route('/teams/search')
def teams_search():
	return "teamsearch"

if __name__ == '__main__':
	app.run()