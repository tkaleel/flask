from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if 'count' in session:
        session['count'] += 1
    else:
        count = 1
        session['count'] = count
    return render_template("index.html")

@app.route('/increment')
def button():
    session['count'] += 2
    return render_template("index.html")

@app.route('/choose')
def input():
    print(request.form)
    # choice = request.form['choice']
    # session['count'] += choice
    return render_template("index.html")

@app.route('/destroy_session')
def clear():
    print("Clearing Session...")
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

