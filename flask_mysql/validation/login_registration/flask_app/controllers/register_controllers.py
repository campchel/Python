from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.register_model import Register
from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)



#attaches the home html page to the server above
@app.route('/')
@app.route('/register')
def home():
    return render_template("register_login.html")

#registering a new user
@app.route('/create', methods=['POST'])
def create_Register():
    if not Register.validate_Register(request.form):
# redirect to the route where the registration form is.
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    newReg={
    'first_name' : request.form['first_name'],
    'last_name' : request.form['last_name'],
    'email' : request.form['email'],
    'password' : pw_hash
}
    Regid=Register.create(newReg)
    session['Regid'] = Regid
    return redirect(f'/newReg')


#logging in
@app.route('/login', methods=['POST'])
def login():
    email = {'email' : request.form['email']}
    newReg = Register.get_email(email)
    if not newReg:
        flash('invalid email or password')
        return redirect('/')
    if not bcrypt.check_password_hash(newReg.password, request.form['password']):
        flash('invalid email or password')
        return redirect('/')
    session['Regid']= newReg
    return redirect('/newReg')

@app.route('/newReg')
def logged_in():
    if 'Regid' not in session:
        return redirect('/')
    return render_template('newReg.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
