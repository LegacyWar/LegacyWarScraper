from github import Github
import json

with open('config.json') as config_file:
    config = json.load(config_file)

username = config['github']['username']
password = config['github']['password']

g = Github(username, password);

for repo in g.get_user().get_repos():
    print repo.name
