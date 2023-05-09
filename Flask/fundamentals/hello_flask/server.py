from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/play/<int:num>')      #make a route inside() that you will type the url
def block_number(num):
    return render_template('playground.html',num=num)  # Return the html template and the number parameter   

@app.route('/play/<int:num>/<string:color>') # make a route inside () that you will type the url with multiple factors
def block_color(num,color):
    return render_template('playground.html',num=num,color=color) # Return the html template and multiple parameters  

if __name__=="__main__":    
    app.run(debug=True) #should be the very last statement!

    
# example  route setup

# @app.route('/<string:name>') # @app.route('/Chelsey')
# def Name(name):#               def say_name():
#     return f'Hello, {name}'#     return 'Hello, Chelsey'
