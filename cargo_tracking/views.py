from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import User
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
                if radioValue == "adminT" and request.user.role == "ADMIN":
                    return redirect("adminpaneli")

                elif radioValue == "courierT" and request.user.role == "COURIER":
                    return redirect("kuryepaneli")

                elif radioValue == "userT" and request.user.role == "CUSTOMER":
                    return redirect("kullanicipaneli")

        else:
           return render(request, "girisyap")
    return render(request, "girisyap.html")

@user_passes_test(lambda u: not u.is_authenticated)
def kayitol(request):
    if (request.method == 'POST'):
        email = request.POST.get("emailR")
        phone = request.POST.get("phoeR")
        name= request.POST.get("nameR")
        lastname = request.POST.get("lastnameR")
        password1 = request.POST.get('password1R')
        password2 = request.POST.get("password2R")
        username = request.POST.get("usernameR")
        if (password1 == password2):
            if (User.objects.filter(email=email).exists()):
                messages.error(request, "Email mevcut")
                return redirect("kayitol")
            elif(User.objects.filter(user_name=username).exists()):
                messages.error(request, "Kullanıcı adı mevcut")
                return redirect("kayitol")
            else:
                user = User.objects.create_user(email=email,  password=password1, phone=phone, user_name=username, first_name=name, last_name=lastname, role="CUSTOMER")    
                user.save()
                # messages.success(request, "Hesabınız başarılı bir şekilde oluşturuldu")
                return redirect("girisyap")
        elif(password1 != password2):
            messages.error(request, "Şifre tekrarı hatalı")
            return redirect("kayitol")

    return render(request, "kayitol.html")


## Admin Views

@login_required
@user_passes_test(lambda u: u.role == "ADMIN")
def adminpaneli(request):
    is_admin_panel = request.resolver_match.url_name == 'adminpaneli'

    return render(request, "adminpaneli.html")

@login_required
@user_passes_test(lambda u: u.role == "ADMIN")
def yenigonderim(request):
    return render(request, "yenigonderim.html")

@login_required
@user_passes_test(lambda u: u.role == "ADMIN")
def gonderiyonet(request):
    return render(request, "gonderiyonet.html")

@login_required
@user_passes_test(lambda u: u.role == "ADMIN")
def tamamlanmis(request):
    return render(request, "tamamlanmis.html")

@login_required
@user_passes_test(lambda u: u.role == "ADMIN")
def kuryetakip(request):
    return render(request, "kuryetakip.html")
##

## Courier Views

@user_passes_test(lambda u: u.role == "COURIER")
@login_required
def kuryepaneli(request):
    return render(request, "kuryepaneli.html")
##

## User Views

@login_required
@user_passes_test(lambda u: u.role == 'CUSTOMER')
def kullanicipaneli(request):
    return render(request, "kullanicipaneli.html")
##

@login_required
def hesapayarlari(request):
    return render(request, "hesapayarlari.html")

def hakkimizda(request):
    return render(request, "hakkimizda.html")

def logout_view(request):
    logout(request)
    response = redirect('anasayfa')
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response
        
def navbar(request):
    return render(request, "navbar.html")

def kargohareketleri(request):
    return render(request, "kargohareketleri.html")
