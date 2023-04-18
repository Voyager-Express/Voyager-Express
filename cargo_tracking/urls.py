from django.urls import path
from . import views

urlpatterns = [
    path("", views.anasayfa, name="anasayfa"),
    ## Admin ##
    path("adminpaneli", views.adminpaneli, name="adminpaneli"),
    path("adminpaneli/yenigonderim", views.yenigonderim, name="yenigonderim"),
    path("adminpaneli/gonderiyonet", views.gonderiyonet, name="gonderiyonet"),
    path("adminpaneli/kuryetakip", views.kuryetakip, name="kuryetakip"),
    path("adminpaneli/tamamlanmis", views.tamamlanmis, name="tamamlanmis"),
    ## ##
    path("kullanicipaneli", views.kullanicipaneli, name="kullanicipaneli"),
    path("kuryepaneli", views.kuryepaneli, name="kuryepaneli"),
    ## Genel ##
    path("hakkimizda/", views.hakkimizda, name="hakkimizda"),
    path("kayitol", views.kayitol, name="kayitol"),
    path("navbar", views.navbar, name="navbar"),
    path("hesapayarlari", views.hesapayarlari, name="hesapayarlari"),
    path("girisyap", views.girisyap, name="girisyap"),
    path("logout", views.logout_view, name='logout'),
    ## ##
    
]