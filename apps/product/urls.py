from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import *


router = DefaultRouter()
router.register('product', ProductViewSet, basename='product')
router.register('review', ReviewViewSet, basename='review')

urlpatterns = [
    path('', include(router.urls)),
]