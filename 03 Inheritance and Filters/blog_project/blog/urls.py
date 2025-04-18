from django.urls import path
from .views import article_list, about_view, contact_view

urlpatterns = [
    path('', article_list, name='article_list'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),

]