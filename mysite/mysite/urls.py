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
    url(r'^blog/', 'polls.views.blog', name='blog'),
    url(r'^pricing/', 'polls.views.pricing', name='pricing'),
    url(r'^contact-us/', 'polls.views.contactus', name='contact-us'),
    url(r'^about-us/', 'polls.views.aboutus', name='about-us'),
    url(r'^blog-item/', 'polls.views.blogitem', name='blog-item'),
    url(r'^portfolio/', 'polls.views.portfolio', name='portfolio'),
    url(r'^services/', 'polls.views.services', name='services'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

