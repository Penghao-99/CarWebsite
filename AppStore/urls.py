"""AppStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import app.views

# path('website',views.py method, method name)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app.views.login, name='login'),           ########## penghao to cheng hong: ideally once admin login, the website should go to ..../personalinfo   
    path('index', app.views.index, name='index'),                        ########     |
    path('signup', app.views.signup, name='signup'),                      #######    \|/
    path('personalinfo', app.views.personalinfo, name='personalinfo'),    ####### should go to this line 
    path('personalcarinfo', app.views.personalcarinfo, name='personalcarinfo'),
    path('tunavailablecarinfo', app.views.unavailablecarinfo, name='unavailablecarinfo'),
    path('rentalcarinfo', app.views.rentalcarinfo, name='rentalcarinfo'),
   #path('add', app.views.add, name='add'),
    path('addpersonalinfo', app.views.addpersonalinfo, name='addpersonalinfo'),    ######## add info dont need special coz it'll always go same page same empty fields
    path('addpersonalcarinfo', app.views.addpersonalcarinfo, name='addpersonalcarinfo'),   ######### edit info then need coz diff row diff displayed info in fields
    path('addunavailablecarinfo', app.views.addunavailablecarinfo, name='addunavailablecarinfo'),
    path('addrentalcarinfo', app.views.addrentalcarinfo, name='addrentalcarinfo'),
    
    path('login', app.views.login, name='login'),
    
    path('personalinfo/edit/<str:id>', app.views.editpersonalinfo, name='editpersonalinfo'),  ##### how to choose 2 columns instead of 1 coz I want composite pri key
    path('personalcarinfo/edit/<str:id>', app.views.editpersonalcarinfo, name='editpersonalcarinfo'),  ##### and what is <str:id> ? can <str:email>????
    path('unavailablecarinfo/edit/<str:id>', app.views.editunavailablecarinfo, name='editunavailablecarinfo'), ### goes to html file editunavailablecarinfo.html 
                                                                                                               ### to retrieve <str:id> from {{cust.0}}
    path('rentalcarinfo/edit/<str:id>/<str:id2>', app.views.editrentalcarinfo, name='editrentalcarinfo'),
    
    path('profile', app.views.profile, name='profile'),
   #path('view/<str:id>', app.views.view, name='view'),
   #path('edit/<str:id>', app.views.edit, name='edit'),
]

