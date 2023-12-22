from django.urls import path 
from . import views
#from django.conf.urls import url

urlpatterns = [ 
         #path('', views.index), 
         path("book/",views.BookApiView.as_view()),

] 