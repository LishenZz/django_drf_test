from django.urls import path
from . import  views
app_name='drf'

urlpatterns=[
    path('get',views.get_test,name='get_test'),
]