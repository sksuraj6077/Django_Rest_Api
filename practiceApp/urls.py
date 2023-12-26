from django.urls import path , include
from . import views
from rest_framework import routers
#from django.conf.urls import url

router = routers.DefaultRouter()
router.register(r'companies',views.CompanyViewSet)
router.register(r'employees',views.EmployeeViewSet)

urlpatterns = [ 
         path("book/",views.BookApiView.as_view()),
         path('',include(router.urls))

] 
