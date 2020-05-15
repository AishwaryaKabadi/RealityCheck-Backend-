from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('Reality_Verifier_App', views.PictureView)

urlpatterns = [path('', include(router.urls)), path('UploadImage/',
               views.UploadImage.as_view(),
               name='UploadImage')]
