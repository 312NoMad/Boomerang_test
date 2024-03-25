from django.urls import path

from .views import *


urlpatterns = [
    path('add-to-cart/', AddToCart.as_view(), name='add-to-cart'),
    path('create-order/', CreateOrder.as_view(), name='create-order'),
    path('cart/', MyCartView.as_view(), name='my-cart')
]
