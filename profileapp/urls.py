from django.urls import path, include
from rest_framework.routers import  DefaultRouter
from . import views

app_name = 'profileapp'


router = DefaultRouter()
router.register('hellowviewset',views.HellowViewSet, basename='hellowviewset')


urlpatterns = [
    path('hellowview/',views.HelloApiView.as_view()),
    path('',include(router.urls))
]
