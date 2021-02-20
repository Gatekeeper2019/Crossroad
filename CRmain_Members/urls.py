from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('login/', views.login_user, name='login'),
   path('logout/', views.logout_user, name='logout'),
   path('dash/', views.dash, name='dash'),
   path('pastordash/', views.pastordash, name='pastordash'),
   path('testing/', views.testing, name='testing'),
   path('newvisitors', views.newvisitors, name='newvisitors'),
   path('visitor/<int:id>', views.visitor),
   path('churchplant/', views.New_Churches, name='churchplant'),
   path('plant/<int:id>', views.plant),
   path('newintern/', views.newintern, name='newintern'),
   path('interns/<int:id>', views.interns, name='interns'),
   #path('resultsData/<str:obj>', views.resultsData, name="resultsdata"),
]
