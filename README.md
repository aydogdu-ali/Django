# Django 
# Burda Django nasıl kurulur ve django ile path işlemleri nasıl yapıldığı gösterilmiştir. Aşaşıda Detaylı olarak ne yapılması gerektiğini anlattım.
1 - Öncelikle shell’den python versiyonunu kontrol etmek için terminale  python –version  komutunu yazırız. Bu komutla  python versiyonunu görmüş oluruz.
2- Daha sonra terminalde çalışma ortamımızı oluşturmak üzere terminale  python –m venv env komutunu yazarız.( -m: Modül/ env ise dosyamızın ismi uygulamada hep env olarak verilmektedir.)
Vs Code  yukarıdaki komutu yazınca env klasörünün oluştuğunu görürüz.
3- Bu işlemden sonra oluşturduğumuz env klasörünün active hale getiririz. 
Bunun için  source env/Scripts/Activate komutu ile aktif hale getiririz.(Windows için) Bunu anlamak için klasörün kenarında (env) ibaresini görürüz. 
(.env/Scripts/Activate)
4- Pasif hale getirme deactivate komutu ile olur.
5- Django kurmak için hazırız. pip install django komutu ile kurarız. Burada bize  “python.exe -m pip install --upgrade pip” böyle bir uyarı vermektedir. 
Bu komut satırını da çalıştırıp pip’in en son versiyonunu yükleriz.
6- pip freze komutu ile  kurduğumuz paketleri görürüz. pip freze > requirements.txt bu bizim kurduğumuz paketleri proje içerisinde sabitler. 
Her paket kurulumundan sonra çalıştırmak bizim için faydalıdır.
7- Daha sonra env klasörümüzün bulunduğu dizinde “.gitignore” dosyası oluşturuyoruz.
https://www.toptal.com/developers/gitignore/api/django  içeriğini buradan alıyoruz.
8- Eğer oluşturduğumuz sanal ortama env ismi vermeseydik farklı bir isim verseydik bunu gitignore dosyasının
#Enviroments kısmında belirtmemiz gerekecektir(örnek myenv/ gibi)
9- Yukarıda temel kurulumları yaptıktan sonra projemizi oluşturacağımız klasörü kurma işlemine geçeriz. 
Bunun için django-admin startproject main . (main ismi vermek yaygın olarak verilen isim)
şekilde görüldüğü gibi main dosyası oluşur. Burada __init__.py dosyası bu uygulamanın python dosyası olduğunu gösteririr.
asgi.py ve wsgi.py ise bunlar serverlar için arayüz. Python direkt serveri göremediği için bunları kullanır.
Setting.py ise configirasyonları yapıyoruz.
Debug=true geliştirme ortamında true deployment ortamında false
Urls.py ise  yönlendirmeleri yapıyoruz.
10 -Daha sonra kurduğumuz proje dosyası sonrası projenin çalıştığını kontrol etmek için terminale python manage.py runserver yazarız.
 
11- Burada bize çalışacağız localhostu gösterir. Ayrıca otomatik olarak oluşturulan veri tabanı ile ilgili de uyarı mesajı verir. Bunları migrate etmemiz gerekiyor.
Bunun için komut satırına python manage.py migrate yazarız.
Bir projede birden fazla application olabilir. Bunun için python manage.py startapp student dersek student adlı app klasörü oluşur.
Bundan sonra her eklediğimiz app dosyasını settings.py içerisinde bulunan INSTALLED_APPS dosyasının içine ekliyoruz. 
Burada oluşan app de bizim için views e yönlendirme yapıyoruz. Bu yönlendirmeyi Main klasöründe bulunan urls.py dosyası ile yapıyoruz.
Oluşturduğumuz app de bulunan views.py klasöründe class larımızı tanımlıyoruz. Yine burada kullandığımız parametreler var ise import ediyoruz.
Yukarıda tanımladığımız fonksiyonun çalışmasını görmek için Main klasöründe bulunan urls.py dosyasına tanıtıyoruz. 
 

 
 



#UYGULAMALARDA YAYGIN OLARAK KULLANILAN YÖNTEM HER BİR APP DOSYASININ KENDİ URL DOSYASI OLMASI ŞEKLİNDEDİR. 
Bunun amacı settings deki urls.py dosyasının kalabalık ığını ve kodların okunabilirliğini sağlamaktır.
Bunun için her bir app klasöründe urls.py dosyası oluşturulur.   
 
Bunu yaptıktan sonra burada tanımladığımız urls.py dosyasını Main ‘de bulunan urls.py dosyasına import ederiz. Bunun için “include” keywordunu kullanırız.
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('teacher/',include('teacher.urls')),
    path('student/',include('student.urls')),
]
   
