from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/password/", views.PasswordView.as_view(), name="password"),
]
