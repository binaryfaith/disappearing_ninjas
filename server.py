from flask import Flask,render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def user_info():
    return  render_template('allninjas.html')

@app.route('/ninja/<color>')
def color(color):
    if color == "purple":
        image = "/static/ninjas/donatello.jpg"
    elif color == "blue":
        image = "/static/ninjas/leonardo.jpg"
    elif color == "orange":
        image = "/static/ninjas/raphael.jpg"
    elif color == "red":
        image = "/static/ninjas/michelangelo.jpg"
    else: 
        image = "/static/ninjas/notapril.jpg"

    return  render_template('ninja.html', image=image)

app.run(debug=True)



       
