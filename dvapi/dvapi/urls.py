from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from resources import views
from .views import GetToken


router = routers.DefaultRouter()
router.register(r'drugs', views.DrugViewSet)
router.register(r'vaccinations', views.VaccinationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('token/', GetToken.as_view(), name='token_obtain_pair'),
]
