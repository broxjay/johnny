from django.urls import path
from .views import main, detail, contact

urlpatterns = [
    path('', main, name= 'home'),
    path('<int:pk>', detail, name='more info'),
    path('contact', contact, name='contact'),
]