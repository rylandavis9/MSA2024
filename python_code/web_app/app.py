#import modules
from flask import Flask, render_template, request, url_for, redirect, abort, flash
import requests

#create flask app
app = Flask(__name__)
app.config['DEBUG'] = True

#set secret key to use when validating form data

app.config['SECRET_KEY'] = 'tbu'
#function to request student data from the api
#imput URL
#output JSON student data
def get_student_data(url):
    #make request
    response = requests.get(url)

    #convert format to json
    response_json = response.json()

    return response_json

#create route for site index page displaying all student data
@app.route('/', methods=['GET'])
def index():
    #get student data
    #make a request to the student data api url
    url = 'http://127.0.0.1:5000/api/students/all'

    #send student data to the index.html
    student_data = get_student_data(url)

    return render_template('index.html', student_data=student_data)

@app.route('/majors', methods=['GET'])
def majors():
    return render_template('majors.html')

app.run(port=5005)