from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                     
    
@app.route('/')                           
def basic():
    return render_template('index.html', num=4, color="red")

@app.route('/play/<int:num>')
def repeat(num):
    num=int(num)/2
    return render_template('index.html', num=int(num), color="red")

@app.route('/play/<int:num>/<int:num2>')
def repeatTwice(num, num2):
    num=int(num)/2
    num2=int(num2)/2
    return render_template('index.html', num=int(num), num2=int(num2), color="red")

@app.route('/play/<int:num>/<color>')
def repeat_color(num, color):
    num=int(num)/2
    return render_template('index.html', num=int(num), color=color, )


if __name__=="__main__":
    app.run(debug=True)                   
