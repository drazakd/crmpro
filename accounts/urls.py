from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('adminreg',views.adminreg,name='adminreg'),
    path('log_out',views.logout_view,name='log_out')
]