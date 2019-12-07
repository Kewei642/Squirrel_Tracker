from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.all_squirrels, name="all"),
    path('add/', views.add_squirrel, name="add"),
    path('<squirrel_id>/', views.squirrel_details, name="detail"),
    path('<squirrel_id>/edit/', views.edit_squirrel, name="edit_squirrel"),
]