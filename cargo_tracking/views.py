from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import User, Cargo, Courier, Cities
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.cache import never_cache
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from django.shortcuts import get_object_or_404


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
                    courierI = Courier.objects.all()
                    for data in courierI:
                        if (data.courier_id == request.user.id):
                            return redirect("kuryepaneli")
                    Courier(courier_id = request.user.id, 
                            courier_name = (request.user.first_name + " " + request.user.last_name),
                            active_cargo_count = 0).save()

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
        phone = request.POST.get("phoneR")
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
    cityList = Cities.objects.all()
    timeNow = datetime.now()
    
    if (request.method == "POST"):
        # sender_customer_id_value = request.POST.get("")
        ## TEMP
        cargo_name_value = request.POST.get("cargo_nameF")
        sender_first_name_value = request.POST.get("sender_nameF")
        sender_last_name = request.POST.get("sender_nameF")
        sender_address_value = request.POST.get("sender_addressF")
        sender_city_value = request.POST.get("cbCitySenderF")
        sender_phone_value = request.POST.get("sender_phoneF")
        # reciever_customer_id_value
        reciever_first_name_value = request.POST.get("reciever_nameF")
        reciever_last_name_value = request.POST.get("reciever_nameF")
        reciever_address_value = request.POST.get("reciever_addressF")
        reciever_city_value = request.POST.get("cbCityRecieverF")
        reciever_phone_value = request.POST.get("reciever_phoneF")
        cargo_type_value = request.POST.get("cbTypeF")
        cargo_feature_value = request.POST.get("cbFeatureF")
        cargo_edt_value = request.POST.get("cbDeliveryTimeF")
        delivery_date_value = timeNow
        courier_id_value = None

        courierI = Courier.objects.all()

        for i in courierI:
            if (i.city == reciever_city_value and i.active_cargo_count <= i.cargo_limit):
                courier_id_value = i.courier_id
                i.active_cargo_count += 1
                break
        try:
            new_instance = Cargo(cargo_name = cargo_name_value,
                                sender_first_name = sender_first_name_value,
                                sender_last_name = sender_last_name,
                                sender_address = sender_address_value,
                                sender_city = sender_city_value,
                                sender_phone = sender_phone_value,
                                reciever_first_name = reciever_first_name_value,
                                reciever_last_name = reciever_last_name_value,
                                reciever_address = reciever_address_value,
                                reciever_city = reciever_city_value,
                                reciever_phone = reciever_phone_value,
                                cargo_type = cargo_type_value,
                                cargo_feature = cargo_feature_value,
                                cargo_edt = cargo_edt_value,
                                delivery_date = delivery_date_value,
                                courier_id = courier_id_value,
                                stage = 0)
            new_instance.save()
            return redirect("adminpaneli")
        except:
            return redirect("yenigonderim")

    return render(request, "yenigonderim.html", {
        "currentDate" : timeNow,
        "CityList" : cityList
    })

@login_required
@user_passes_test(lambda u: u.role == "ADMIN")
def gonderiyonet(request):
    cargoList = Cargo.objects.all()

    return render(request, "gonderiyonet.html", {
        "CargoList" : cargoList,
    })

@login_required
@user_passes_test(lambda u: u.role == "ADMIN")
def tamamlanmis(request):
    cargoList = Cargo.objects.all()
    courierList = Courier.objects.all()
    return render(request, "tamamlanmis.html", {
        "CargoList" : cargoList,
        "CourierList" : courierList,
    })

@login_required
@user_passes_test(lambda u: u.role == "ADMIN")
def kuryetakip(request):
    courierList = Courier.objects.all()
    cityList = Cities.objects.all()
    return render(request, "kuryetakip.html", {
        "CourierList" : courierList,
        "CityList" : cityList
    })

@login_required
@user_passes_test(lambda u: u.role == "ADMIN")
def updateCourier(request):
    if (request.method == "POST"):
        courier_id_value = request.POST.get("courier_idF")
        city_value = request.POST.get("city_nameF")
        cargo_limit_value = request.POST.get("cargo_limitF")
        active_cargo_value = request.POST.get("active_cargoF")

        courier = Courier.objects.get(pk=courier_id_value)   
        # courier(cargo_limit = cargo_limit_value, city = city_value)
        try:
            courier.cargo_limit = int(cargo_limit_value)
            courier.city = city_value
        except:
            return redirect("kuryetakip")
        courier.save()
        return redirect("kuryetakip")
    return redirect("kuryetakip")
    


def updateCargoStageAdmin(request):
    if (request.method == "POST"):
        cargoID = request.POST.get("cargo_idF")
        radio_value = request.POST.get("options")
        
        cargo = Cargo.objects.get(pk=cargoID)

        if (radio_value == "stage0"):
            cargo.stage = 0
        elif (radio_value == "stage1"):
            cargo.stage = 1
        elif (radio_value == "stage2"):
            cargo.stage = 2
        elif (radio_value == "stage3"):
            cargo.stage = 3
        cargo.save()
        return redirect("gonderiyonet")

    return redirect("gonderiyonet")
            

## End of Admin Views

## Courier Views

@user_passes_test(lambda u: u.role == "COURIER")
@login_required
def kuryepaneli(request):
    cargoList = Cargo.objects.all()

    return render(request, "kuryepaneli.html", {
        "CargoList" : cargoList,
        "CourierID" : request.user.id
    })

@login_required
@user_passes_test(lambda u: u.role == "COURIER")
def updateCargoStageCourier(request):
    if (request.method == "POST"):
        cargoID = request.POST.get("cargo_idF")
        radio_value = request.POST.get("options")
        
        cargo = Cargo.objects.get(pk=cargoID)
        
        if (radio_value == "stage1"):
            cargo.stage = 1
        elif (radio_value == "stage2"):
            cargo.stage = 2
        elif (radio_value == "stage3"):
            cargo.stage = 3
        cargo.save()
        return redirect("kuryepaneli")

    return redirect("kuryepaneli")
## End of Courier Views

## User Views

@login_required
@user_passes_test(lambda u: u.role == 'CUSTOMER')
def kullanicipaneli(request):    
    cargoList = Cargo.objects.all()
    currUser = User.objects.get(pk=request.user.id)

    return render(request, "kullanicipaneli.html", {
        "CargoList" : cargoList,
        "CurrUser" : currUser,
    })
## End of User Views

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
    userRole = None
    if request.user.is_authenticated:
        userRole = request.user.role
    print(userRole)
    return render(request, "navbar.html", {
        "UserRole" : userRole
    })

def kargohareketleri(request):
    currCargoId = request.POST.get('cargo_id')
    print(currCargoId)
    # cargo = Cargo.objects.get(pk=currCargoId)
    cargo = get_object_or_404(Cargo, pk=currCargoId)
    return render(request, "kargohareketleri.html", {
        "CurrentCargo" : cargo
    })

def kargodetay(request):
    cargoId = request.POST.get("cargo_idF")
    cargo = get_object_or_404(Cargo, pk=cargoId)
    print(cargoId)
    return render(request, "kargodetay.html", {
        "ActiveCargo" : cargo
    })
