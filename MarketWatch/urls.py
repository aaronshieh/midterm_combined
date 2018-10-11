from django.urls import path
from MarketWatch import views

app_name='MarketWatch'

urlpatterns = [
    path('', views.index),
    path('personallist/',views.personallist)
]