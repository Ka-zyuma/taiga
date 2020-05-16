from django.urls import path
from . import views
from .views import InfoRegister
urlpatterns = [
    path('index/', views.info, name='info' ),
    path('info/register/', InfoRegister.as_view(), name='register' ),
]
