from flask import Flask, render_template, request, flash, redirect
from flask.helpers import url_for
from flask_mysqldb import MySQL
from authentication import check_password, encrypt_password

app = Flask(__name__)
# ----database connect----

# host will be local host once moved to pi
app.config['MYSQL_HOST'] = '192.168.254.156'
# this will be root once moved to pi
app.config['MYSQL_USER'] = 'remoteUser'
app.config['MYSQL_PASSWORD'] = 'Orkz9921('
app.config['MYSQL_DB'] = 'todoList'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

# server testing


@app.route('/databaseTest')
def test():
    cur = mysql.connection.cursor()
    cur.execute('''select * from Users ''')
    results = cur.fetchall()
    print(results)
    return '<h1>Pi Change</h1>'


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def signIn():
    if request.method == 'POST':
        url = request.url
        # getting infor from the form
        data = request.form
        username = data.get('username')
        password = data.get('password')
        # now has to check database
        cur = mysql.connection.cursor()
        # this will check if the user exist
        try:
            cur.execute(
                f"select username from Users where username='{username}'")
            # checking the Username
            database_username = cur.fetchone()['username']
            print(database_username)
            # checking the password
            try:
                cur.execute(
                    f"select password from Users where username='{username}'")
                database_password = cur.fetchone()
                database_password = database_password['password']
                if(check_password(database_password, password)):
                    # where it will redirect user once it loads
                    return f"<h1>Hello {database_username}</h2>"
            except:
                flash('password incorrect', category='error')
                return render_template('login.html')
        except:
            flash('Username or Password is incorrect', category='error')
            return render_template('login.html')
    else:
        return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signUp():
    if request.method == 'POST':
        data = request.form
        # gets data from the form
        email = data.get('email')
        confirm_email = data.get('confirm_email')
        username = data.get('username')
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        # checking if all data exist
        if email == '' or confirm_email == '' or username == '' or password == '' or confirm_email == '':
            flash('Missing sign-up data try again', category='error')
            return render_template('signup.html')
        # none matching data
        else:
            if email != confirm_email:
                flash('Emails must match', category='error')
                return render_template('signup.html')
            elif password != confirm_password:
                flash('Passwords must match', category='error')
                return render_template('signup.html')
        # enter the info to the data base then return user to login with a positive alert
            else:
                cur = mysql.connection.cursor()
                hashed_password = encrypt_password(password)
                # trys to create the user
                try:
                    cur.execute(
                        f"insert into Users values('{email}', '{username}' , '{hashed_password}')")
                    mysql.connection.commit()
                    return redirect(url_for('signIn'))
                # if user can't be created it will flash an error
                except:
                    flash('Email or User already exist', category='error')
                    return render_template('signup.html')
    else:
        return render_template('signup.html')


if __name__ == '__main__':
    app.secret_key = 'pie123'
    app.run(debug=True, host='0.0.0.0')
