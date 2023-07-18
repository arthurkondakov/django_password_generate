from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='home'),
    path('info/', views.info_page),
    path('password/', views.password, name="password"),
    path('about/', views.aboutpage, name='aboutpage')
]