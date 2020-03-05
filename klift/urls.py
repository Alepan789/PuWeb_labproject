
from django.urls import path
from klift.views import KliftIndex
from klift.views import KliftBlog

urlpatterns = [
    path('', KliftIndex.as_view()),
    path('', KliftBlog.as_view()),
]
