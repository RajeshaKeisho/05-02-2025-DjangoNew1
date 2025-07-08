from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('sample/', views.sample_view, name='sample_view'),  

]