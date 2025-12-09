from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('main_menu/', views.main_menu, name='main_menu'),
    path('s30_la_miel/', views.la_miel_list, name='s30_la_miel'),
]
