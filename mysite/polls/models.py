from django.db import models
import json
# Create your models here.
from pymongo import MongoClient
client = MongoClient()
client = MongoClient('localhost', 27017)

db = client.mydb


def getDockcounts(city):
    data =[]
    jsonData = []
    for post in db.station_data.find({"landmark":city}, { "name": 1, "lat": 1, "dockcount": 1, "_id":0, "installation":1 }):
        data.append(post)
    
    #Store array in json object
    jsonData=json.dumps(data)            
    print ("json object :", jsonData)
    
    #Iterate over json object
    temp = json.loads(jsonData)
    #for i in temp:
    #    print (i['name'])
    return jsonData
 
def getSeasoncounts(day):
    day_type = 1
    if day == 'holiday':
        pipeline = [{ '$match' : {'holiday' : day_type}},{ '$group' : { '_id' : '$season', 'total' : { '$sum' : 1 } }}]
        res= db.command('aggregate','train',pipeline=pipeline)
        jsondata = json.dumps(res)

        print(jsondata)   
    elif day == 'workday':
        pipeline = [{ '$match' : {'workingday' : day_type}},{ '$group' : { '_id' : '$season', 'total' : { '$sum' : 1 } }}]
        res= db.command('aggregate','train',pipeline=pipeline)
   
        jsondata = json.dumps(res)
        print(jsondata)
          
    return jsondata   

def station_information(city):
    temp = []
    tempjsonData= []
    jsonData =[]
    #print("abc",db.station_data.find({ "landmark": "San Jose", "name":1,"_id": 0})
    for doc in db.station_data.distinct("name",{"landmark": city}):
    #print("abcdefgh", db.station_data.find({ "landmark": "San Jose", "name":1,"_id": 0})):
    #print("here is the array", doc)
        temp.append(doc)
        
    tempjsonData=json.dumps(temp)
    jsonData = trip_information(tempjsonData)  
    print("jsonData ",jsonData)         
    return jsonData

def trip_information(tempjsonData):
    xzy = []
    out = json.loads(tempjsonData)
    data= []
    for i in out:
        pipeline = [{ '$match' : {"Start Station" : i}},{ '$group' : { '_id' : "$Subscriber Type", 'total' : { '$sum' : 1 } }}]
        res= db.command('aggregate','trip_data',pipeline=pipeline)
        data.append(res)
    data.remove(res)
    jsonoutput = json.dumps(data)
    return jsonoutput
   
def station_name(city):
    temp = []
    jsonData =[]
    #print("abc",db.station_data.find({ "landmark": "San Jose", "name":1,"_id": 0})
    for doc in db.station_data.distinct("name",{"landmark": city}):
    #print("abcdefgh", db.station_data.find({ "landmark": "San Jose", "name":1,"_id": 0})):
    #print("here is the array", doc)
        temp.append(doc)
        
    jsonData=json.dumps(temp)
    return jsonData 