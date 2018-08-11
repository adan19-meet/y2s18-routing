from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home_route():
    return render_template(
    	"home.html")

app.run(debug=True)

@app.route('/student/<int:student_id>')
def display_student(student_id):
	return render_template("student.html", n=student_id)

app.run(debug=True)
