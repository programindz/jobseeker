from django.urls import path
from . import views

urlpatterns= [
    path('', views.jobseeker_homepage, name = 'home'),
    path('signup/', views.signup_with_resume, name = 'signup_with_resume')
]