'''
Created on 22 mar. 2017

@author: jeiglesias
'''

import requests, json

def headerAuth():
    psw = 'QmlyY2htYW5cR2VybWFuLlBhbG1hOkJpcmNobWFuMjAyMA=='
    hdr = {"Authorization": "Basic "+psw,
           "Content-Type": "application/json" }
    return hdr

def createStep(instanceId):
    url = "https://secure.p03.eloqua.com"+"/api/REST/2.0/data/customObject/31/instance"
    jsonReq = {
    "type": "CustomObjectData",
    "fieldValues": [
        {
            "id": "387",
            "value": instanceId
        }
    ]
    }
    res = requests.post(url,json=jsonReq, headers=headerAuth())
    return res

def saveStep(instanceId, type, subtype, sr):
    url = "https://secure.p03.eloqua.com"+"/api/REST/1.0/assets/contact/segment/123"
    res = requests.get(url,headers=headerAuth())
    return res

    print res.status_code
    print res.headers['content-type']
    print json.dumps(res.json(), indent=4)