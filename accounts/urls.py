from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('adminsignup',views.adminsignup,name='adminsignup'),
    path('log_out',views.logout_view,name='log_out')
]