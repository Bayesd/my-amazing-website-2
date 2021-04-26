import gspread
from flask import Flask, render_template, request as r
app = Flask(__name__)

gc = gspread.service_account(filename='flask-hemsida.json')
sh = gc.open('flask-website')

shProfile = sh.get_worksheet(0)
shContacts = sh.get_worksheet(1)


@app.route('/', methods=['POST', 'GET'])
def home():
    if r.method == 'POST':
        shContacts.append_row([r.form['name'], r.form['email'], r.form['message']])
    
    profile = {
        'about':shProfile.acell('B1').value,
        'interests':shProfile.acell('B2').value,
        'experience':shProfile.acell('B3').value,
        'education':shProfile.acell('B4').value
    }
    return render_template("index.html", profile=profile)

@app.route('/contact')
def contact():
    return render_template("contact.html")
