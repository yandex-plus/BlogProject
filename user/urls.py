from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login_page, name='login_page'),
    path('registration/', views.registration, name='registration_page'),
]
