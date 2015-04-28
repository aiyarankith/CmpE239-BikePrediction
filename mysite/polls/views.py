from django.shortcuts import render
import json
# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from polls.models import models, getDockcounts, getSeasoncounts, station_information, station_name
from django.core.serializers.json import DjangoJSONEncoder
import pandas as pd
import numpy as np
import csv 

from dateutil.parser import parse
from sklearn.ensemble import RandomForestRegressor
from sklearn import ensemble
from sklearn.metrics import mean_absolute_error
from sklearn.grid_search import GridSearchCV
from datetime import datetime
import os.path
from django.core.files.storage import default_storage
import mysite

def index(request):
    request.session.flush()

    template = loader.get_template('index.html')
    context = RequestContext(request, {

    })
    return HttpResponse(template.render(context))

def weatherstat(request):
    template = loader.get_template('weatherstat.html')
    context = RequestContext(request, {
        
    })
    return HttpResponse(template.render(context))

def pricing(request):
    template = loader.get_template('pricing.html')
    context = RequestContext(request, {
        
    })
    return HttpResponse(template.render(context))
def aboutus(request):
    template = loader.get_template('about-us.html')
    context = RequestContext(request, {
        
    })
    return HttpResponse(template.render(context))
def portfolio(request):
    template = loader.get_template('portfolio.html')
    context = RequestContext(request, {
        
    })
    return HttpResponse(template.render(context))
def blogitem(request):
    template = loader.get_template('blog-item.html')
    context = RequestContext(request, {
        
    })
    return HttpResponse(template.render(context))
def contactus(request):
    template = loader.get_template('contact-us.html')
    context = RequestContext(request, {
        
    })
    return HttpResponse(template.render(context))

def services(request):
    template = loader.get_template('services.html')
    context = RequestContext(request, {
        
    })
    return HttpResponse(template.render(context))

#DockCount Details
def bikedock(request):
    template = loader.get_template('bikedock.html')
    
    #session set
    if 'session_set' in request.session:
        print ("inside session if")
        del request.session['session_set']
        request.session.flush()
        request.session['session_set']=getDockcounts("San Jose")
    else:
        request.session['session_set']=getDockcounts("San Jose")        
        
    context = RequestContext(request, {
        "var_city":"San Jose",
        "session":request.session['session_set']
    })
    return HttpResponse(template.render(context))

#DockCount Details
def generate_dock_details(request):
    template = loader.get_template('bikedock.html')
    print("city :",request.GET["city"])
    
    #session set
    if 'session_set' in request.session:
        print ("inside session if")
        del request.session['session_set']
        request.session.flush()
        request.session['session_set']=getDockcounts(request.GET["city"])
        print ("session set: ",request.session['session_set'])
    else:
        request.session['session_set']=getDockcounts(request.GET["city"])
    
    context = RequestContext(request, {
        "var_city":request.GET["city"],
        "session":request.session['session_set']
    })
    return HttpResponse(template.render(context))
    
#Prediction Algorithm
def predictsale(request):
    if 'dt' in request.POST:
        path1 = default_storage.open('mysite\\train.csv')
        path2 = default_storage.open('mysite\\test.csv')

        train_data = pd.read_csv(path1, parse_dates=[0])
        test_data = pd.read_csv(path2, parse_dates=[0])
    
        dt = request.POST['dt']
        d = parse(dt)
        test_data['day'] = d.day
        test_data['month'] = d.month
        test_data['year'] = d.year
        test_data['hour'] = d.hour
        test_data['season'] = int(request.POST['season'])
    
        test_data['temp'] = float(request.POST['temp'])
        test_data['atemp'] = float(request.POST['atemp'])
        test_data['humidity'] = int(request.POST['humidity'])
        test_data['windspeed'] = float(request.POST['windspeed'])
    
        weather_condition = request.POST['weather']
        if weather_condition=='Clear' or weather_condition=='Partly Cloudy' or weather_condition=='Very Hot':
            test_data['weather'] = 1
        if weather_condition=='Mostly Cloudy' or weather_condition=='Cloudy' or weather_condition=='Hazy' or weather_condition=='Chance of Showers' or weather_condition=='Chance of Rain' or weather_condition=='Chance of Showers' :
            test_data['weather'] = 2
        if weather_condition=='Very Cold' or weather_condition=='Showers' or weather_condition=='Rain' or weather_condition=='Chance of a Thunderstorm' or weather_condition=='Flurries' or weather_condition=='Chance of Snow Showers' or weather_condition=='Snow Showers' or weather_condition=='Chance of Snow':
            test_data['weather'] = 3
        if weather_condition=='Foggy' or weather_condition=='Blowing Snow' or weather_condition=='Thunderstorm' or weather_condition=='Snow' or weather_condition=='Ice Pellets' or weather_condition=='Chance of Ice Pellets' or weather_condition=='Blizzard':
            test_data['weather'] = 4
    
   
        dt_train = pd.DatetimeIndex(train_data['datetime'])
        train_data['year'] = dt_train.year
        train_data['month']= dt_train.month
        train_data['hour'] = dt_train.hour
        train_data['day'] = dt_train.day
    
        for colum in ['casual', 'registered', 'count']:
            train_data['log-' + colum] = train_data[colum].apply(lambda x: np.log1p(x))
    
        attrib = ['year','month', 'day', 'hour','season', 'weather','temp', 'atemp', 'humidity', 'windspeed']
     
        gbr = ensemble.GradientBoostingRegressor(n_estimators=80, learning_rate = .05, max_depth = 10,min_samples_leaf = 20)
   
        casual_pred= gbr.fit(train_data[attrib].values, train_data['log-casual'].values)
        registered_pred= gbr.fit(train_data[attrib].values, train_data['log-registered'].values)
        total = np.expm1(casual_pred.predict(test_data[attrib])) + np.expm1(registered_pred.predict(test_data[attrib]))
        
        print("sale :",total)
        return render(request, 'predictsale.html', {'total_sale': int(total[0]), 'date': dt})

    else:    
        return render(request, 'predictsale.html')

#Season Count
def seasoncount(request):
   # request.session.flush()
    #template = loader.get_template('seasondock.html')
    holidaycount = getSeasoncounts("holiday")
    workdaycount = getSeasoncounts("workday")
    print ('holiday:',holidaycount)
    print ('workday:',workdaycount)
    return render(request, 'seasondock.html', {'holiday': holidaycount, 'workday': workdaycount})
 
#Top Stations 
def topstations(request):
    template = loader.get_template('top_start_end_station.html')
    station_list = [22788, 15679, 13555, 12741, 11653]
    context = RequestContext(request, {
        "station_list":station_list
    })
    return HttpResponse(template.render(context)) 
   
   
def generate_station_details(request):
    request.session.flush()
    template = loader.get_template('customeranalysis.html')
    #request.session[v]
    #post = json.dumps(station_information(), cls=DjangoJSONEncoder)
    context = RequestContext(request, {
        "station_details":station_information("San Jose"),
        "city_names":station_name("San Jose")
    })
    return HttpResponse(template.render(context))

#station details
def customeranalysis(request):
    template = loader.get_template('customeranalysis.html')
    print request.GET["city"]
    context = RequestContext(request, {
        "station_details":station_information(request.GET["city"]),
        "city_names":station_name(request.GET["city"])
    })
    return HttpResponse(template.render(context))
   
   
def demo_form(request):
    template = loader.get_template('demo_form.html')
    context = RequestContext(request, {
        
    })
    return HttpResponse(template.render(context))
def add_details(request):
    print(request.GET["name"])
    template = loader.get_template('result_of_form.html')
    context = RequestContext(request, {
        "req_name":request.GET["name"]
    })
    return HttpResponse(template.render(context))