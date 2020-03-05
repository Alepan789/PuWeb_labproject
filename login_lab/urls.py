
from django.urls import path
from login_lab.views import LoginView
from login_lab.views import LoginAbout
# import login_lab.views

urlpatterns = [
    path('', LoginView.as_view()),
    path('about/', LoginAbout.as_view()),
]
