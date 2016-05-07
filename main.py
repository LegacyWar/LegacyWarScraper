from github import Github
import json
import pymongo
from flask import Flask

app = Flask(__name__)

with open('config.json') as config_file:
    config = json.load(config_file)

username = config['github']['username']
password = config['github']['password']


@app.route('/')
def data():
    g = Github(username, password);

    items = []
    for repo in g.get_user().get_repos():
        items.append(repo.name)

    return json.dumps(items)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
