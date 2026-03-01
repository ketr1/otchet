from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login'),
    path('guest/', views.guest_page, name='guest'),
    path('products/', views.product_list_page, name='products'),

    path("logout/", views.logout, name="logout"),
]