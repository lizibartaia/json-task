from django.urls import path

from . import views

urlpatterns = [
    path("", views.selectAnimalView.as_view(), name="selectAnimalView"),
    path("create/", views.addAnimalView.as_view(), name="addAnimalView"),
    path("delete/<int:pk>", views.deleteAnimalView.as_view(), name="deleteAnimalView")
]