
from django.urls import path
from .views import teacher # teacher app inde bulunan views dosyasından teacher class ını import et aynı klasörde bulunduğumuzdan başına nokta koyarak import ederiz.

urlpatterns = [
       
    path('', teacher), # Main urls.py dosyasında teacher gelirse buraya gelir ve views daki teacher classındaki fonksiyonu gösterir. 
]
