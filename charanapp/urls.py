from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('send',views.submit,name='sumbit'),
    path('login',views.login,name='login'),
]
