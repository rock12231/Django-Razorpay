from django.urls import path
from pay import views

urlpatterns = [
       path('', views.index, name='homepage'),
]
