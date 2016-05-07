import os
import json

from github import Github
from pymongo import MongoClient
from flask import Flask, jsonify
from bson import json_util

from Scraper.ScraperModel import ScraperModel

app = Flask(__name__)

with open('config.json') as config_file:
    config = json.load(config_file)

username = config['github']['username']
password = config['github']['password']

docker_port_id = "LEGACYWAR_DB_1_PORT_27017_TCP_ADDR"
client = MongoClient(os.environ[docker_port_id], 27017)
db = client.test

model = ScraperModel(db)

@app.route('/')
def data():
    _repos = model.buildLeaderboard()
    repos = [(repo['full_name'], repo['repository_commits']) for repo in _repos]
    return jsonify(repos=repos)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
