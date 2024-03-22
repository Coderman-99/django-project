from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Char_detail
from django.contrib.auth.models import User, auth
from django.contrib import messages

characters = [
    "albedo",
    "aloy",
    "amber",
    "ayaka",
    "ayato",
    "barbara",
    "beidou",
    "bennett",
    "childe",
    "chongyun",
    "collei",
    "diluc",
    "diona",
    "eula",
    "fischl",
    "ganyu",
    "gorou",
    "heizou",
    "kazuha",
    "keqing",
    "klee",
    "kaeya",
    "jean",
    "itto",
    "hutao",
    "kokomi",
    "lisa",
    "mona",
    "ningguang",
    "noelle",
    "qiqi",
    "raiden",
    "razer",
    "sara",
    "sayu",
    "shenhe",
    "shinobu",
    "sucrose",
    "thoma",
    "tighnari",
    "venti",
    "xiangling",
    "xiao",
    "xingqiu",
    "xinyan",
    "yae",
    "yanfei",
    "yoimiya",
    "yunjin",
    "zhongli",
]
# Create your views here.
# def index1(request):
#     feature1 = Features()
#     feature1.id = 888888
#     feature1.is_true = True
#     feature1.service_name = "back massage"
#     feature1.details = "very good back massage"

#     feature2 = Features()
#     feature2.id = 88888
#     feature1.is_true = False
#     feature2.service_name = "foot massage"
#     feature2.details = "very good foot massage"

#     feature3 = Features()
#     feature3.id = 88888877
#     feature3.is_true = True
#     feature3.service_name = "hand massage"
#     feature3.details = "very good hand massage"

#     features = Features.objects.all
#     return render(
#         request,
#         "index.html",
#         {"features": features},
#     )


def logout(request):
    auth.logout(request)
    return redirect("/")


def post(request, pk):
    return render(request, "post.html", {"pk": pk})


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("sucessful")
        else:
            messages.info(request, "wrong username or password. Try again!")
            return redirect("login")
    else:
        return render(request, "login.html")


def sucessful(request):
    return render(request, "sucessful.html")


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "email already used")
                return redirect("register")
            elif User.objects.filter(username=username).exists():
                messages.info(request, "username alreay used")
                return redirect("register")
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password
                )
                user.save()
                return redirect("login")
        else:
            messages.info(request, "passwords are not the same")
            return redirect("register")
    else:
        return render(request, "register.html")


# def search(request):
#     search = request.GET["search"]
#     for character in characters:
#         if search == character:
#             search = character
#             break
#     search_html = search + ".html"
#     return render(request, search_html, {"search": search_html})


def index(request):
    by_name = request.GET.get("by_name", "by_name_asc")
    by_ele = request.GET.get("by_ele", "default")
    if by_name == "by_name_asc":
        if by_ele == "default":
            character = Char_detail.objects.all().order_by("name")
        elif by_ele == "by_pyro":
            character = Char_detail.objects.filter(vision="pyro").order_by("name")
        elif by_ele == "by_cryo":
            character = Char_detail.objects.filter(vision="pyr").order_by("name")
        elif by_ele == "by_electro":
            character = Char_detail.objects.filter(vision="electro").order_by("name")
        elif by_ele == "by_hydro":
            character = Char_detail.objects.filter(vision="hydro").order_by("name")
        elif by_ele == "by_anemo":
            character = Char_detail.objects.filter(vision="anemo").order_by("name")
        elif by_ele == "by_dendro":
            character = Char_detail.objects.filter(vision="dendro").order_by("name")
        else:
            character = Char_detail.objects.filter(vision="geo").order_by("name")
    else:
        if by_ele == "default":
            character = Char_detail.objects.all().order_by("-name")
        elif by_ele == "by_pyro":
            character = Char_detail.objects.filter(vision="pyro").order_by("-name")
        elif by_ele == "by_hydro":
            character = Char_detail.objects.filter(vision="hydro").order_by("-name")
        elif by_ele == "by_electro":
            character = Char_detail.objects.filter(vision="electro").order_by("-name")
        elif by_ele == "by_cryo":
            character = Char_detail.objects.filter(vision="cryo").order_by("-name")
        elif by_ele == "by_dendro":
            character = Char_detail.objects.filter(vision="dendro").order_by("-name")
        elif by_ele == "by_anemo":
            character = Char_detail.objects.filter(vision="anemo").order_by("-name")
        else:
            character = Char_detail.objects.filter(vision="geo").order_by("-name")

    return render(request, "index.html", {"characters": character})


def character(request, pk):
    mat = Char_detail.objects.get(id=pk)
    character = Char_detail.objects.get(id=pk)
    character.asc_mat1 = character.asc_mat1.replace(" ", "_")
    character.asc_mat1 = character.asc_mat1.replace(" ", "_")
    character.asc_mat2 = character.asc_mat2.replace(" ", "_")
    character.asc_mat3 = character.asc_mat3.replace(" ", "_")
    character.asc_mat4 = character.asc_mat4.replace(" ", "_")
    character.asc_rock1 = character.asc_rock1.replace(" ", "_")
    character.asc_rock2 = character.asc_rock2.replace(" ", "_")
    character.asc_rock3 = character.asc_rock3.replace(" ", "_")
    character.asc_rock = character.asc_rock.replace(" ", "_")
    character.boss_mat = character.boss_mat.replace(" ", "_")
    return render(request, "character.html", {"pk": character, "mat": mat})


def counter(request):
    chars = ["haha", "loll", "hhasdh", "jfhdj"]
    return render(request, "counter.html", {"chars": chars})
