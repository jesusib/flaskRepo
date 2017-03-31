from flask import Flask, flash, redirect, render_template, request, url_for, jsonify
from flask_cors import CORS, cross_origin
from flask.helpers import send_file, send_from_directory
from src import urls
import os
from flask_sslify import SSLify

app = Flask(__name__)
app.secret_key ='random string'
sslify = SSLify(app)
#CORS(app)


#Keep until dev is completed
@app.route('/')
def index():
    return render_template('ConfigForm.html')

@app.route('/enable/')
def checkStatus():
    resp = jsonify()
    resp.status_code = 200
    return resp

@app.route('/create/<instance>', methods=['POST', 'GET'])
def createInstance(instance):
    data =    {
        "recordDefinition":{
            "ContactID" : "{{Contact.Id}}",
            "EmailAddress" : "{{Contact.Field(C_EmailAddress)}}"
            }
    }
    resp = jsonify(data)
    
    apiC = apiCalls.createStep(instance)
    if(apiC.status_code != 200):
            resp.status_code = 500
            
    resp.status_code = 200
    return resp

@app.route('/icon/')
def icon():
    return send_from_directory('templates', 'icon.png')

#@app.route('/icon32/')
#def icon32():
    #return send_from_directory('templates', 'icon-circle32.jpg')

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
   
   
'''
from OpenSSL import SSL
context = SSL.Context(SSL.SSLv23_METHOD)
context.use_privatekey_file('server.key')
context.use_certificate_file('server.crt')

def emptyOK():
    resp = jsonify()
    resp.status_code = 200
    return resp'''