from flask import Flask, render_template, redirect, session, request, url_for
from db import get_all_items, get_items_by_id, add_item
app = Flask(__name__, template_folder='./front-end', static_folder='static')

@app.route('/')
def home():
    return render_template('home/home.html', items=get_all_items())

@app.route('/catalog/<id>')
def catalog(id):
    item = get_items_by_id(id)[0]

    if item:
        return render_template('catalog.html', title=item[1], description=item[3], imgURL=item[2])
        
    return redirect('/')

app.run(debug=True)

