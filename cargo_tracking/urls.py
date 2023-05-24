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
    path("adminpaneli/updateCourier", views.updateCourier, name="kuryeGuncelle"),
    path("adminpaneli/gonderiyonet/updateCargoStage", views.updateCargoStageAdmin, name="updateCargoStageAdmin"),
    path("adminpaneli/kuryepaneli/updateCargoStage", views.updateCargoStageCourier, name="updateCargoStageCourier"),
    path("kargodetay", views.kargodetay, name='kargodetay'),
    ## ##

    ## Kurye ##
    path("kuryepaneli", views.kuryepaneli, name="kuryepaneli"),
    ## ##

    ## Kullanici ##
    path("kullanicipaneli", views.kullanicipaneli, name="kullanicipaneli"),
    ## ##

    ## Genel ##
    path("hakkimizda/", views.hakkimizda, name="hakkimizda"),
    path("kayitol", views.kayitol, name="kayitol"),
    path("navbar", views.navbar, name="navbar"),
    path("hesapayarlari", views.hesapayarlari, name="hesapayarlari"),
    path("girisyap", views.girisyap, name="girisyap"),
    path("logout", views.logout_view, name='logout'),
    path("kargohareketleri", views.kargohareketleri, name='kargohareketleri'),
    ## ##
    



    
]