from bson.son import SON

class ScraperModel:
    def __init__(self, db):
        self.db = db

    def getRepositories(self):
        _items = self.db.repositories.find()
        return [ item for item in _items ]

    def getLeaderboard(self):
        criteria = {
            'date': '05/06/2016',
            'scoring_method': 'default'
        };
        _leaderboards = self.db.leaderboards.find(criteria)
        result = _leaderboards[0] if _leaderboards else {};

        return result

    def buildLeaderboard(self):
        pipeline = [
            {"$limit": 10},
            {"$sort": SON([("count", -1), ("_id", -1)])},
            {"$lookup": {
                'from': 'commits',
                'localField': 'full_name',
                'foreignField': 'full_name',
                'as': 'repository_commits'
            }}
        ]
        _reps = self.db.repositories.aggregate(pipeline)
        return [ repo for repo in _reps ]
