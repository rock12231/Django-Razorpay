from django.urls import path
from pay.views import Home
from pay import views
urlpatterns = [
       path('', Home.as_view(), name='home'),
       path('profile/', views.Login, name='login'),
       path('', views.Logout, name='logout'),   
]
