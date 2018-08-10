from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
from flaskext.mysql import MySQL
from wtforms import Form,StringField,PasswordField,TextAreaField,validators
from  passlib.hash import sha256_crypt
from functools import  wraps
from flask_mail import Mail,Message
from itsdangerous import URLSafeTimedSerializer,SignatureExpired

app = Flask(__name__)

app = Flask(__name__)

app.config['SECRET_KEY'] = 'greatworks-yes'
app.config.update(

	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
    MAIL_USE_TLS=False,
	MAIL_USERNAME = 'choudarypavansai@gmail.com',
	MAIL_PASSWORD = 'Spring2017csc93'
	)
mail = Mail(app)

s=URLSafeTimedSerializer(app.config['SECRET_KEY'])
#Config MySQL
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='12345'
app.config['MYSQL_DATABASE_DB']='application'
app.config['MYSQL_CURSORCLASS']='DictCursor'
#app.config['MYSQL_DATABASE_PORT']=3306
#init MYSQL
mysql = MySQL()
mysql.init_app(app)


@app.route('/message/')
def index():
    # Create cursor
    conn = mysql.connect()
    cur = conn.cursor()
    cur.execute("UPDATE users SET status = 1 where username=%s ", name)
    conn.commit()
    cur.close()
    return render_template('confirm_email.html')


@app.route('/')
def homepage():
    return render_template('main.html')

@app.route('/Home/')
def Home():
    return render_template('Home.html')

@app.route('/Contact Us/')
def ContactUs():
    return render_template('About Us.html')

class SignUp(Form):
    name=StringField('Name',[validators.Length(min=3, max=50)])
    username=StringField('Username',[validators.Length(min=4,max=25)])
    email=StringField('Email',[validators.Length(min=6,max=40)])
    password=PasswordField('Password',[validators.DataRequired(),
                                       validators.EqualTo('confirm',message='Passwords do not match each')])
    confirm=PasswordField('Confirm Password')
name=''
@app.route('/Sign Up/',methods=['GET','POST'])
def Signup():
    form=SignUp(request.form)
    if request.method=='POST' and form.validate():
        name=form.name.data
        email=form.email.data
        username=form.username.data
        password=sha256_crypt.encrypt(str(form.password.data))

        token=s.dumps(email,salt='email-confirm')
        msg=Message('Confirm Email',sender='choudarypavansai@gmail.com', recipients=[email])

        link=url_for('confirm_email', token=token, _external=True)

        msg.body='Click the link for activation of your account {}'.format(link)

        mail.send(msg)

        #return redirect(url_for('confirmemail'))

        #ceate cursor
        conn = mysql.connect()
        cur = conn.cursor()

        cur.execute("INSERT INTO users(name,email,username,password) VALUES(%s,%s,%s,%s)",(name,email,username,password))

        #commit to DB
        conn.commit()

        #Close connection
        cur.close()

        flash('You are now registered and can log in','success')

        return redirect(url_for('index'))
       # return render_template('confirm_email.html')
    return render_template('Sign Up.html',form=form)

@app.route('/confirm_email/<token>')
def confirm_email(token):
    try:
        email=s.loads(token,salt='email-confirm',max_age=300)
    except SignatureExpired:
        return 'The token expired'

    return render_template('login.html')


@app.route('/Login/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        #get Form fields
        username=request.form['username']
        password_candidate=request.form['password']
        #Create cursor
        conn = mysql.connect()
        cur = conn.cursor()


        # getuser by username


        result=cur.execute("SELECT * FROM users WHERE username=%s",[username])
        name=result
        #cur.execute("UPDATE users SET status = 1 ")
        if result>0:

            data=cur.fetchone()

            password=data[4]

            #Compare paasswords
            if sha256_crypt.verify(password_candidate,data[4]):
                app.logger.info('PASSWORD MATCHED')
                session['logged_in']=True
                session['username']=username

                flash('Logged in','success')
                return  redirect(url_for('dashboard'))
            else:
                error='Invalid login'
                return render_template('login.html', error=error)

            # Close Connection
            cur.close()

        else:
            error='Username not found'
            return render_template('login.html',error=error)
    return render_template('login.html')

#check whether logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:


            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please Login', 'danger')
            return  redirect(url_for('login'))
    return  wrap





# Logout
@app.route('/Logout/')
def logout():
    session.clear()
    flash('Successfully logged out','success')
    return redirect(url_for('login'))




#dashboard
@app.route('/Dashboard/')
@is_logged_in
def dashboard():
    return  render_template('dashboard.html')

if __name__ == '__main__':
    app.secret_key='secret567'
    app.run(debug=True)

