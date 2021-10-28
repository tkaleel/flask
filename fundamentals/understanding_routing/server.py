import re
from flask import Flask  
app = Flask(__name__)    
@app.route('/')         
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<whatever>')
def say(whatever):
    return whatever

@app.route('/repeat/<num>/<whatever>')
def repeat(num, whatever):
    new_num = int("num")
    
    # for x in range(new_num):
    #     return whatever

#Code below should ALWAYS be at the bottom of server.py file
if __name__=="__main__":     
    app.run(debug=True) 