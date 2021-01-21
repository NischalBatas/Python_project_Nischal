from django.urls import path

from . import views

urlpatterns=[
   path('',views.indexs,name='indexs'),
   path('contact/',views.contact,name='contact'),
   path('result/', views.result, name='result')
   
   
]