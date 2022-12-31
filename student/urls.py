
from django.urls import path
from .views import home # student app inde bulunan views dosyasından home class ını import et 
#aynı klasörde bulunduğumuzdan başına nokta koyarak import ederiz.

urlpatterns = [
       
    path('', home), # Main urls.py dosyasında student gelirse buraya gelir 
    #ve views daki home classındaki fonksiyonu gösterir. 
]
