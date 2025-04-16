
from django.contrib import admin
from django.urls import path, include
from app2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include("myapp.urls")),
     path('register/', views.registration),
    path('login/', views.login),
    path('logout/', views.logout),
]
