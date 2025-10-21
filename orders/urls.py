from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path('create/', views.order_create, name="order_create"),
]
