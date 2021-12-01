from django.contrib import admin
from django.urls import path
from django.urls import include, path
from . import views
app_name='user'
urlpatterns = [
    # path('signup',views.signup , name='signup'),
    path('profile',views.profile , name='profile'),
    # path('profile/edit',views.profile_edit , name='profile_edit'),

]
