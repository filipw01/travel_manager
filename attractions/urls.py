from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cities/', views.cities, name='cities'),
    path('cities/<int:city_id>/', views.city, name='city'),
    path('cities/<int:city_id>/<int:attraction_id>', views.attraction, name='attraction'),
]
