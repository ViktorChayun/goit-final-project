from django.urls import path

from . import views

app_name = 'news'

urlpatterns = [
    path('', views.currency_view, name='main'),
]
