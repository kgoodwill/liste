from flask import Flask
from flask.ext.pymongo import PyMongo
app = Flask(__name__)
mongo = PyMongo(app)

@app.route('/')
def hello_world():
	return "Hello World"

@app.route('/<ObjectId:listid>/')
def get_list(listid):
	shopping = mongo.db.lists.find_one(listid)


@app.route('/<ObjectId:listid>/add')
def add_to_list(listid)
	request.data['listitem']
	mongo.db.lists.update({$push: listitem})
if __name__ == '__main__':
	app.run()
