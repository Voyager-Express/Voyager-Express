from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from . import models
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.cache import never_cache
from django.contrib.auth.mixins import LoginRequiredMixin


def anasayfa(request):
    return render(request, "anasayfa.html") 

def girisyap(request):
    if request.method == "POST":
        radioValue = request.POST.get("options")
        username = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if radioValue == "adminT" and request.user.rol == "ADMIN":
                    return redirect("adminpaneli")

                elif radioValue == "courierT" and request.user.rol == "COURIER":
                    print("staff")
                    return redirect("kuryepaneli")

                elif radioValue == "userT" and not request.user.is_staff and not request.user.rol == "CUSTOMER":
                    print("user")
                    return redirect("kullanicipaneli")

        else:
           return redirect("girisyap")

    return render(request, "girisyap.html")


## Admin Views

@login_required
@user_passes_test(lambda u: u.rol == "ADMIN")
def adminpaneli(request):
    is_admin_panel = request.resolver_match.url_name == 'adminpaneli'

    return render(request, "adminpaneli.html")

@login_required
@user_passes_test(lambda u: u.rol == "ADMIN")
def yenigonderim(request):
    return render(request, "yenigonderim.html")

@login_required
@user_passes_test(lambda u: u.rol == "ADMIN")
def gonderiyonet(request):
    return render(request, "gonderiyonet.html")

@login_required
@user_passes_test(lambda u: u.rol == "ADMIN")
def tamamlanmis(request):
    return render(request, "tamamlanmis.html")

@login_required
@user_passes_test(lambda u: u.rol == "ADMIN")
def kuryetakip(request):
    return render(request, "kuryetakip.html")
##

## Courier Views

@user_passes_test(lambda u: u.rol == "COURIER")
@login_required
def kuryepaneli(request):
    return render(request, "kuryepaneli.html")
##

## User Views

@login_required
@user_passes_test(lambda u: u.rol == 'CUSTOMER')
def kullanicipaneli(request):
    return render(request, "kullanicipaneli.html")
##

@login_required
def hesapayarlari(request):
    return render(request, "hesapayarlari.html")

def hakkimizda(request):
    return render(request, "hakkimizda.html")

@user_passes_test(lambda u: not u.is_authenticated)
def kayitol(request):
    return render(request, "kayitol.html")

def logout_view(request):
    logout(request)
    response = redirect('anasayfa')
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

def navbar(request):
    return render(request, "navbar.html")
