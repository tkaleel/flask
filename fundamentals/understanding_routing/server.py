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

@app.route('/repeat/<int:num>/<string:whatever>')
def repeat(num, whatever):
    output = ''
    
    for i in range(0,num):
        output += f"<p>{whatever}"
    
    return output
# @app.route('/repeat/<int:num>/<string:word>')
# def repeat_word(num, word):
#     output = ''

#     for i in range(0,num):
#         output += f"<p>{word}</p>"

#     return output

#Code below should ALWAYS be at the bottom of server.py file
if __name__=="__main__":     
    app.run(debug=True) 