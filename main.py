from flask import Flask, render_template, redirect
#from pymongo import MongoClient
#import json

app = Flask(__name__)
#app.config.from_file('config.json', load=json.load)

@app.route('/')
def main():
    return render_template('base.html')

@app.route('/create')
def create():
    return render_template('index.html')

    

if __name__ == '__main__':
    app.run(debug=True)
