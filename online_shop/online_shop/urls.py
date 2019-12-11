from django.urls import include, path
from rest_framework.routers import DefaultRouter
from orders import views


router = DefaultRouter()
router.register(r'orders', views.OrderViewSet, basename='order')


urlpatterns = [
    path('', include(router.urls)),
]
