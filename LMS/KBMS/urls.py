from django.urls import path

from . import views

urlpatterns = [
    # ex: /KBMS/
    path('', views.index, name='index'),
    # ex: /KBMS/5/
    path('<str:KitBoard_ID>/', views.detail, name='detail'),
]
