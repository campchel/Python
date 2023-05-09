from flask import Flask, render_template

app=Flask(__name__)

@app.route('/lists') #URL 
def html_table():

    table_info = [
        {'First Name': 'Michael', 'Last Name' : 'Choi'},
        {'First Name' : 'John', 'Last Name': 'Supsupin'},
        {'First Name' : 'Mark', 'Last Name' : 'Guillen'}
    ]


    return render_template("html_table.html", table = table_info)

if __name__=="__main__":
    app.run(debug=True)