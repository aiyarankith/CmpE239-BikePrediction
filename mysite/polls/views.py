from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from polls.models import models, find_document

def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        "abc":find_document()
    })
    return HttpResponse(template.render(context))

def blog(request):
    template = loader.get_template('blog.html')
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
def portfolio(request):
    template = loader.get_template('portfolio.html')
    context = RequestContext(request, {
        
    })
    return HttpResponse(template.render(context))
def services(request):
    template = loader.get_template('services.html')
    context = RequestContext(request, {
        
    })
    return HttpResponse(template.render(context))