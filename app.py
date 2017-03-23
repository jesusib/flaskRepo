from flask import Flask, flash, redirect, render_template, request, url_for, jsonify
from src import urls
import os
from flask.helpers import send_file, send_from_directory


app = Flask(__name__)
app.secret_key = 'random string'

def emptyOK():
    resp = jsonify()
    resp.status_code = 200
    return resp

#Keep until dev is completed
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enable/')
def checkStatus():
    return emptyOK()

@app.route('/create/<instance>', methods=['POST', 'GET'])
def createInstance(instance):
    data =    {
        "recordDefinition":{
            "ContactID" : "{{Contact.Id}}",
            "EmailAddress" : "{{Contact.Field(C_EmailAddress)}}"
            }
    }

    resp = jsonify(data)
    resp.status_code = 200
    return resp


@app.route('/icon/')
def icon():
    img = 'templates'
    return send_from_directory('templates', 'icon.png')


@app.route('/icon32/')
def icon32():
    img = 'templates'
    return send_from_directory('templates', 'icon-circle32.jpg')

@app.route('/icon16/')
def icon16():
    img = 'templates'
    return send_from_directory('templates', 'icon-circle16.jpg')

if __name__ == '__main__':
    #Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    
   #app.debug = True
   #app.run()