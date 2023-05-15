from flask import Flask, render_template, redirect, request
from users import User

app=Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    # passing all users to our template so we can display them there
    return render_template("read_all.html",users= User.get_all())

@app.route('/user/new')
def new():
    return render_template("create.html")

@app.route('/user/create', methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')

if __name__=="__main__":
    app.run(debug=True)