from django.shortcuts import render

# Create your views here.


def anasayfa(request):
    return render(request, "anasayfa.html") 

def adminpaneli(request):
    return render(request, "adminpaneli.html")

def girisyap(request):
    return render(request, "girisyap.html")

def gonderiyonet(request):
    return render(request, "gonderiyonet.html")

def hakkimizda(request):
    return render(request, "hakkimizda.html")

def hesapayarlari(request):
    return render(request, "hesapayarlari.html")

def kayitol(request):
    return render(request, "kayitol.html")

def kullanicipaneli(request):
    return render(request, "kullanicipaneli.html")

def kuryepaneli(request):
    return render(request, "kuryepaneli.html")

def kuryetakip(request):
    return render(request, "kuryetakip.html")

def tamamlanmis(request):
    return render(request, "tamamlanmis.html")

def yenigonderim(request):
    return render(request, "yenigonderim.html")

def navbar(request):
    return render(request, "navbar.html")
