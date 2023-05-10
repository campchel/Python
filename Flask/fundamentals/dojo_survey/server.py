from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key='keep it secret, keep it safe'


@app.route('/name')
def entername():
	return render_template('dojo_survey.html')

@app.route('/process', methods=['POST'])
def process():
	print("processing")
	session['survey_data']={
		'name':request.form['name'],
	'location' : request.form['location'],
	'language' : request.form['language'],
	'description' : request.form['description']
    }
	
	# return render_template('dojo_survey_info.html', sd=survey_data)
	return redirect('/result') #never render post

@app.route('/result')
def result():
	return render_template('dojo_survey_info.html')

if __name__=="__main__":
    app.run(debug=True)