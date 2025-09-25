from django.urls import path
from api import views

urlpatterns = [
    path('api/items/', views.post, name='post'),
    path('api/items/', views.get, name='get')
]