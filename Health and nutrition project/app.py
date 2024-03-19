from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient



app = Flask(__name__)
app.secret_key = 'moni@123'
# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/Mark')
db = client['Mark']   
collection = db['point'] 


@app.route('/')
def Home():
    return render_template('Home page.html')

@app.route('/Recipes')
def Recipes():
    return render_template('Recipes.html')

@app.route('/Contact')
def Contact():
    return render_template('Contact.html')

@app.route('/Lunch')
def Lunch():
    return render_template('Lunch.html')

@app.route('/Dinner')
def Dinner():
    return render_template('Dinner.html')

@app.route('/Juices')
def Juices():
    return render_template('Juices.html')

@app.route('/Search')
def Search():
    return render_template('Search.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Check if the username already exists in the database
        existing_user = collection.find_one({'username': username})
        if existing_user:
            return 'Username already exists. Please choose a different username.'

        # Create a new user document
        new_user = {
            'username': username,
            'email': email,
            'password': password
        }

        # Insert the user document into the collection
        result = collection.insert_one(new_user)

        # Redirect to the login page after successful signup
        return redirect(url_for('login'))

    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username and password match in the database
        user = collection.find_one({'username': username, 'password': password})
        if user:
            # User authenticated successfully, store user's login status in session
            session['username'] = username
            return redirect(url_for('Home'))  # Redirect to Home page

        return 'Invalid credentials. Please try again.'

    return render_template('Loginpage.html')


@app.route('/Breakfast')
def Breakfast():
    return render_template('Breakfast.html')



if __name__ == '__main__':
    app.run(debug=True)