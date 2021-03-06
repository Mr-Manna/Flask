from flask import Flask, render_template, request,session,url_for,redirect
from model import db
from form import SignupForm


app = Flask(__name__)

app.secret_key = "devlopment"

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/flask'
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/home')
def home():
    return render_template('home.html')


# noinspection PyUnreachableCode
@app.route('/signup',methods=['GET', 'POST'])
def signup():
    form = SignupForm()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('signup.html', form=form)
        else:
            newUser = User( form.first_name.data,form.last_name.data,form.email.data )
            db.session.add(newUser)
            db.session.commit()
            session['email'] = newUser.email
            return redirect(url_for('home'))

    elif request.method == 'GET':
        return render_template('signup.html',form = form)


