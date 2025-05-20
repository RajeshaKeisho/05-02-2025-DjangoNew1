from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    # path('under_construction/', views.under_construction, name='under_construction'),
    path('sample/', views.sample_view, name='sample_view'),  # URL for sample_view
]