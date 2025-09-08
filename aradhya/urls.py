from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('interninspot/', views.interninspot, name='interninspot'),
    path('dermascan/', views.dermascan, name='dermascan')
]