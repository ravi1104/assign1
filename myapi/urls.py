from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.api_alldata, name='alldata'),
    path('list/<int:pk>',views.api_listdata,name='listdata')
]