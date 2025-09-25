from django.urls import path
from api import views

urlpatterns = [
    path('api/items/post_news/', views.post, name='post'),
    path('api/items/get_news/', views.get_news, name='get_news'),
]