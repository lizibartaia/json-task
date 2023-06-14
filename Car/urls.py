from django.urls import path

from . import views

urlpatterns = [
    path("", views.selectCarView.as_view(), name="selectCarView"),
    path("create/", views.addCarView.as_view(), name="addCarView"),
    path("delete/<int:pk>", views.deleteCarView.as_view(), name="deleteCarView")
]