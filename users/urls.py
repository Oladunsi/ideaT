from django.conf.urls import url
from .views import RegistrationView

urlpatterns = [
  	url('register/', RegistrationView.as_view()),
]