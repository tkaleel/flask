from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                     
    
@app.route('/')                           
def hello_world():
    return render_template('index.html')

@app.route('/play/<int:num>')
def repeat(num):
    for i in range(0,num):
        return render_template('index.html', num=num, color="blue")

@app.route('/play/<int:num>/<color>')
def repeat_color(num, color):
    for i in range(0,num):
        return render_template('index.html', num=num, color=color)


if __name__=="__main__":
    app.run(debug=True)                   
