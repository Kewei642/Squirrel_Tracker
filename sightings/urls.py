from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_squirrels, name="index"),
    path('add/', views.add_squirrel, name="add"),
    path('stats/', views.stats, name="stats"),
    path('<squirrel_id>/', views.edit_squirrel, name="edit_squirrel"),
]
