from django.urls import path
from vehiculo.views import index, CustomLoginView, CustomLogoutView, RegisterView,vehiculolist_view, vehiculoform_view,contact, subscribe

urlpatterns = [
    path('', index, name='index'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', CustomLogoutView.as_view(), name='logout'),
    path('accounts/register/', RegisterView.as_view(), name='register'),
    path('vehiculo/list/', vehiculolist_view, name="vehiculo_list"),
    path('vehiculo/form/', vehiculoform_view, name="vehiculo_add"),
    path('contact/', contact, name='contact'),
    path('subscribe/',subscribe, name='subscribe'),
]