from flask import render_template, request, redirect

from flask_app import app

from flask_app.models.dojos import Dojo

@app.route('/')
def index():
    return redirect('/dojos')


@app.route('/dojos')
def dojos():
    return render_template("dojos.html", dojos=Dojo.get_all())


@app.route('/dojos/ninja')
def new():
    return render_template("add_ninja.html")


@app.route('/dojo/add',methods=['POST'])
def create():
    print(request.form)
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojo/show/<int:id>')
def show(id):
    data ={ 
        "id":id
    }
    return render_template("dojo_show.html", dojo=Dojo.get_one_dojo_ninjas(data))


