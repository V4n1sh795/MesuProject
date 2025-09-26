from django.urls import path
from api import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/items/post_news/', views.post, name='post'),
    path('api/items/get_news/', views.get_news, name='get_news'),
    path('api/items/post_image/', views.upload_image, name='upload_image'),
    path('api/items/get_images/', views.get_images, name='get_images'),
    path('my-page/', views.my_page, name='page'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)