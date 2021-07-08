from django.urls import path
from . import views

app_name = 'profileapp'

urlpatterns = [
    path('helloview/',views.HelloApiView.as_view()),

]
