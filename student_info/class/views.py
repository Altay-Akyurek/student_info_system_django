from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User

#username entrance "en"
#üyelik giriş "tr"
def user_login(request):
    if request.method =="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return render (request,"uyelik_giriş_deneme.html")
        else:
            return render(request,"uyelik_giriş_deneme.html",{"error":"username or password false"})
    else:
        return render(request,"uyelik_giriş_deneme.html")
#user register "en"
#üyelik giriş "tr"
#user save "en"
#kullanıcı kaydetme "tr"
def user_register(request):
    if request.method=="POST":
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        repassword=request.POST["repassword"]
        
        #user info. control "en"
        #kullanıcı bilgi kontrol "tr"
        if password==repassword:
            if User.objects.filter(username=username).exists():
                return render(request,"kayıt.html",{"error":"bu user name kullanıyor"})
            else:
                if User.objects.filter(email=email).exists():
                    return render(request,"kayıt.html",{"error":"bu eposta ile önceden kayıt yapılmıştır"})
                else:
                    user=User.objects.create_user(username=username,email=email,password=password)
                    user.save()
                    return render(request,"kayıt.html")
        else:
            return render(request,"kayıt.html",{"error":"parolayı ya yanlış ya da eksik tuşladınız"})
        


