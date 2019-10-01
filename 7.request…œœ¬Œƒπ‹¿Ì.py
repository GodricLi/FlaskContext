# by luffycity.com
import redis
from flask import Flask,request,session
from flask.sessions import SecureCookieSessionInterface
from flask_session import Session

app = Flask(__name__)

# app.session_interface = SecureCookieSessionInterface()
# app.session_interface = RedisSessionInterface()
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = redis.Redis(host='140.143.227.206',port=6379,password='1234')
Session(app)

@app.route('/login')
def login():
    session['user'] = 'alex'
    return 'asdfasfd'

@app.route('/home')
def index():
    print(session.get('user'))

    return '...'


if __name__ == '__main__':
    app.run()
    # app.__call__
    # app.wsgi_app