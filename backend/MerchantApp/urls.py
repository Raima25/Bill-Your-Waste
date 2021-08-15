from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    path('merchant/notCollected',views.notCollected,name=''),
    path('merchant/collected',views.collected,name=''),
    path('merchant/totalDue',views.totalDue,name=''),
    path('merchant/totalReceived',views.totalReceived,name=''),
    path('merchant/askCategory',views.askCategory,name=''),
    path('merchant/getCategory',views.getCategory,name=''),
    path('merchant/sell',views.sell,name=''),
    path('merchant/account',views.account,name='')
]