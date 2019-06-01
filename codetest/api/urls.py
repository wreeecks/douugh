from django.urls import path, include
from rest_framework import routers
from .views import ApiUserView, ApiUserLoginView

app_name = "api"
router = routers.DefaultRouter()
router.register('apiuser', ApiUserView)

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    #path('', include(router.urls)),    
    path('create', ApiUserView.as_view(), name="create"),
    path('login', ApiUserLoginView.as_view(), name="login")
]