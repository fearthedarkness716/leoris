from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    path('order/<int:order_id>/pay/', views.order_pay, name='order_pay'),
    path('completed/', views.order_completed, name='order_completed'),
    path('profile/', views.profile_view, name='profile'),
] 