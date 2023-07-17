from django.urls import path
from . import views


urlpatterns = [
path('', views.index, name='index'),
path('property_grid', views.property_grid, name='property_grid'),
path('property/<int:pk>/', views.property_single, name='property_single'),
path('contact', views.contact, name = 'contact'),
path('about', views.about, name = 'about'),

]