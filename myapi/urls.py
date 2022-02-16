from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/<int:pk>',views.apidata,name='apidata')
]