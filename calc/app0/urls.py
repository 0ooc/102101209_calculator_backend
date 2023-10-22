from django.urls import path
from app0 import views
urlpatterns = [
    path('huode/', views.huode),
    path('shangchuan/', views.shangchuan),
]