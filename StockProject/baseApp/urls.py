
from django.urls import path
from baseApp import views
urlpatterns = [
    path('', views.HomeView, name='home'),

]
