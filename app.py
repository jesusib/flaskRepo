from flask import Flask, flash, redirect, render_template, request, url_for
import os
from src import urls
app = Flask(__name__)
app.secret_key = 'random string'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/testRoute')
def testRoute():
    return urls.testRute()





if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    #port = int(os.environ.get('PORT', 5000))
    #app.run(host='0.0.0.0', port=port)
    app.run()
