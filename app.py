from flask import Flask, render_template, request
import pymssql
from flask_basicauth import BasicAuth

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'username'
app.config['BASIC_AUTH_PASSWORD'] = 'password'

basic_auth = BasicAuth(app)

# Connect to the database
server: str = '172.17.0.2'
database: str = 'FLASK_DB'
username: str = 'sa'
password: str = 'Root#123456'
# Connect to the database
cnxn = pymssql.connect(server, username, password, database)
cursor = cnxn.cursor()


@app.route('/')
@basic_auth.required
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
@basic_auth.required
def submit():
    name = request.form['name']
    email = request.form['email']
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    cnxn.commit()
    cursor.close()
    return 'Success'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6350)

