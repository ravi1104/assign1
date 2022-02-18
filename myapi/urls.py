from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'', views.Imageuploadviewset)

urlpatterns = [
    path('viewalldata', views.api_alldata, name='alldataview'),
    path('newupload', include(router.urls)),
    path('viewlist/<int:pk>',views.api_listdata,name='listview')
]