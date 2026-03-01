from django.shortcuts import render, redirect
from django.db.models import Q
from django.http import HttpRequest

from .models import Users, Products, Suppliers


def login_page(request: HttpRequest):
    if request.method == "GET":
        return render(request, "shop/login.html", {"title": "Вход"})

    login = request.POST.get("login", "").strip()
    password = request.POST.get("password", "").strip()

    if not login or not password:
        return render(
            request,
            "shop/login.html",
            {"title": "Вход", "errors": "Введите логин и пароль"},
        )

    try:
        user = Users.objects.select_related("role").get(login=login, password=password)
    except Users.DoesNotExist:
        return render(
            request,
            "shop/login.html",
            {"title": "Вход", "errors": "Неверный логин или пароль"},
        )

    request.session["is_auth"] = True
    request.session["role"] = user.role.role   # roles.role
    request.session["full_name"] = user.fio    # users.fio

    return redirect("/products/")


def guest_page(request: HttpRequest):
    request.session["is_auth"] = False
    request.session["role"] = "гость"
    request.session["full_name"] = "Гость"
    return redirect("/products/")


def product_list_page(request: HttpRequest):
    q = request.GET.get("q", "").strip()
    supplier_id = request.GET.get("supplier", "").strip()
    sort = request.GET.get("sort", "").strip()

    products = Products.objects.select_related("supplier", "discount")

    if q:
        products = products.filter(
            Q(name__icontains=q) |
            Q(description__icontains=q) |
            Q(article__icontains=q)
        )

    if supplier_id.isdigit():
        products = products.filter(supplier_id=int(supplier_id))

    if sort == "stock_asc":
        products = products.order_by("stock_qty")
    elif sort == "stock_desc":
        products = products.order_by("-stock_qty")

    suppliers = Suppliers.objects.order_by("name")

    return render(
        request,
        "shop/products_list.html",
        {
            "title": "Список товаров",
            "full_name": request.session.get("full_name"),
            "role": request.session.get("role"),
            "q": q,
            "supplier_id": supplier_id,
            "sort": sort,
            "products": products,
            "suppliers": suppliers,
        },
    )


def logout(request: HttpRequest):
    request.session.flush()
    return redirect("/")