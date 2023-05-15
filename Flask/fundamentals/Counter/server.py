from flask import Flask, render_template, redirect, session 
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' 




@app.route('/count') # will process the form
def count():
        #ask-is count in session?
        if 'count' in session:
            # if count is in session, increase by 1
            session['count']+=1
        else:
            # hasn't made a session yet add to session
            session['count']=0
        return render_template("counter.html", count=session['count'])


@app.route('/addtwo', methods=['POST'])
def addtwo():
    session['count']+=1
    return redirect('/count')
                                        # Never render a template on a POST request.
                                        # Instead redirect to the index route.
@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/count')


if __name__=="__main__":
    app.run(debug=True)