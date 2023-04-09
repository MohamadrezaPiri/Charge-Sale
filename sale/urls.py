from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('sell', views.SaleOrderViewSet)

urlpatterns = router.urls
