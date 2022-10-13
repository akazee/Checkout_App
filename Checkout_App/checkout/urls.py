from django.urls import path
from . import views

urlpatterns = [
    path('', views.create, name='create'),
    path('<int:id>', views.index, name='index'),
    path("create/", views.create, name="create"),
]