from django.urls import path ,include
from . import views

from django.contrib.auth.models import User
app_name='home'

urlpatterns = [
    path('', views.home, name='home'),  
    path('send-message/', views.send_message, name='send_message'),
    path('sec/<int:mobile_number>/<int:password>', views.sec, name='sec'),
    path('send-messaget/', views.send_messaget, name='send-messaget'),

]