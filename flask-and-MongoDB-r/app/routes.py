import os
import sys
from app import app
from flask import render_template, request, redirect

sys.path.append("/Users/2020rkessler/flask-and-MongoDB/app/")
from models import model

events = [
        {"event":"First Day of Classes", "date":"2019-08-21", "category": "educational"},
        {"event":"Winter Break", "date":"2019-12-20", "category": "fun"},
        {"event":"Finals Begin", "date":"2019-12-01", "category": "educational"},
        {"event":"Summer Vacation","date":"2019-6-01" , "category": "fun"}
    ]


from flask_pymongo import PyMongo

# name of database
app.config['MONGO_DBNAME'] = 'test'

# URI of database
app.config['MONGO_URI'] = 'DATABASE STUFF HERE'

mongo = PyMongo(app)

# INDEX

#@app.route('/')
@app.route('/')
@app.route('/index',methods = ["POST"])
def index():
    events = mongo.db.events
    all_queries = events.find({})
    all_events = {}

    if dict(request.form):
        added_data = dict(request.form)
        event_name = added_data["event_name"]
        date =  added_data["date"]
        all_events[event_name] = date
        events = mongo.db.events
        events.insert({"event":event_name, "date": date})

    return render_template('index.html', events = all_events)

@app.route('/input', methods = ["POST"])
def input():
    return render_template('input.html')

@app.route('/login', methods = ["POST"])
    events = mongo.db.events
    username = "ryan"
    password = "kessler"
    if request.form["delete_all"] == "delete_all":
        return render_template('login.html')
    else:
        if request.form["username"] == username and request.form["password"] == password:
            for event in events.find({}):
                events.delete_one({"event":event["event"]})
            return render_template('index.html')

@app.route('/results', methods = ["GET", "POST"])
def insert_data ():
    added_data = dict(request.form)
    event_name = added_data["event_name"]
    date =  added_data["date"]
    events = mongo.db.events
    events.insert({"event":event_name, "date": date})

    return render_template("results.html", event_name=event_name, date=date)
