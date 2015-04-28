from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from polls.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'polls.views.index', name='index'),
    url(r'^index/', 'polls.views.index', name='index'),
    #url(r'^blog/', 'polls.views.blog', name='blog'),
    #url(r'^predict/', 'polls.views.predictsale', name='pricing'),
    url(r'^contact-us/', 'polls.views.contactus', name='contact-us'),
    url(r'^about-us/', 'polls.views.aboutus', name='about-us'),
    url(r'^blog-item/', 'polls.views.blogitem', name='blog-item'),
    url(r'^portfolio/', 'polls.views.portfolio', name='portfolio'),
    #url(r'^services/', 'polls.views.services', name='services'),
    
    #Bikedock 
    url(r'^bikedock/', 'polls.views.bikedock', name='bikedock'),
    url(r'^generate_dock_details/', 'polls.views.generate_dock_details', name='generate_dock_details'),
    
    #Algorithm Implementation
    url(r'^predictsale/', 'polls.views.predictsale', name='predictsale'),

    #Season Count
    url(r'^seasondock/', 'polls.views.seasoncount', name='seasondock'),
    
    #Top Stations
    url(r'^topstations/', 'polls.views.topstations', name='topstations'),
    
    #generate_station_details Stations
    url(r'^generate_station_details/', 'polls.views.generate_station_details', name='generate_station_details'),
    url(r'^customeranalysis/', 'polls.views.customeranalysis', name='customeranalysis'),
    
    #Weather wise bike sale results
    url(r'^weatherstat/', 'polls.views.weatherstat', name='weatherstat'),
    
    #Example Passing Form elements.
    url(r'^demo_form/', 'polls.views.demo_form', name='demo_form'),
    url(r'^add_details/', 'polls.views.add_details', name='result_of_form'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

