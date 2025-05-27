from flask import Flask, redirect, url_for
from api_routers.auth import router

app = Flask(__name__)
app.register_blueprint(router)

@app.get('/')
def main():
    return redirect(url_for('auth.google_oauth2_authentication'))

'''
use in console from project root directory to get test certificates:

openssl req -x509 -newkey rsa:4096 -keyout certificates/key.pem -out certificates/cert.pem -days 365 -nodes
'''
app.run(ssl_context=("certificates/cert.pem", "certificates/key.pem"))