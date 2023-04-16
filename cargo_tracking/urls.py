from django.urls import path
from . import views

urlpatterns = [
    path("", views.anasayfa, name="anasayfa"),
    path("adminpaneli", views.adminpaneli, name="adminpaneli"),
    path("girisyap", views.girisyap, name="girisyap"),
    path("gonderiyonet", views.gonderiyonet, name="gonderiyonet"),
    path("hakkimizda", views.hakkimizda, name="hakkimizda"),
    path("hesapayarlari", views.hesapayarlari, name="hesapayarlari"),
    path("kayitol", views.kayitol, name="kayitol"),
    path("kullanicipaneli", views.kullanicipaneli, name="kullanicipaneli"),
    path("kuryepaneli", views.kuryepaneli, name="kuryepaneli"),
    path("kuryetakip", views.kuryetakip, name="kuryetakip"),
    path("navbar", views.navbar, name="navbar"),
    path("tamamlanmis", views.tamamlanmis, name="tamamlanmis"),
    path("yenigonderim", views.yenigonderim, name="yenigonderim"),
    path("logout/", views.logout_view, name='logout')
    
]