from flask import render_template, request, redirect

from flask_app import app

# from flask_app.models.ninjas import Ninja

# @app.route('/')
# def index():
#     return redirect('/dojos')


@app.route('/dojos')
def users():
    return render_template("dojos.html",dojos=Dojo.get_all())


@app.route('/dojos/ninja')
def new():
    return render_template("add_ninja.html")


@app.route('/dojo/add',methods=['POST'])
def create():
    print(request.form)
    Dojo.save(request.form)
    return redirect('/dojos')


@app.route('/dojo/edit/<int:id>')
def edit(id):
    data ={ 
        "id":id
    }
    return render_template("edit.html",dojos=Dojo.get_one(data))

@app.route('/dojo/show/<int:id>')
def show(id):
    data ={ 
        "id":id
    }
    return render_template("dojo_show.html",dojo=Dojo.get_one(data))


@app.route('/dojo/update',methods=['POST'])
def update():
    Dojo.update(request.form)
    return redirect('/users')

@app.route('/dojo/destroy/<int:id>')
def destroy(id):
    data ={
        'id': id
    }
    Dojo.destroy(data)
    return redirect('/users')