from django.urls import path
from cal import views

urlpatterns = [
    path('', views.index, name='index'),

]
