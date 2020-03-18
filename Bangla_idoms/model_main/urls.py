from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='home'),
    path('api/data', views.api_data, name='api-data'),
    path('api/district', views.api_district, name='api-district'),
    path('api/chandaKatha', views.api_chandaKatha, name='api-chandakatha')


]
