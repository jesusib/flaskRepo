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

def saveStep(instanceName, type, subtype, sr):
    
    searchUrl = "https://secure.p03.eloqua.com"+"/api/REST/2.0/data/customObject/31/instances?search="+instanceName
    searchRes = requests.get(searchUrl,headers=headerAuth())
    searchResId = searchRes.json()['elements'][0]['id']
    
    url = "https://secure.p03.eloqua.com"+"/api/REST/2.0/data/customObject/31/instance/"+searchResId
    updateInfo = {
    "type": "CustomObjectData",
    "fieldValues": [
        {
            "id": "388",
            "value": type
        },
        {
            "id": "389",
            "value": subtype
         },
         {
            "id": "390",
            "value": sr
         },
        
    ]
    }
    res = requests.put(url,json=updateInfo,headers=headerAuth())
    return res
