from django.contrib import admin
from django.urls import path, include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='main'),
    path('ad_item/', views.create_ad, name='create_ad'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)