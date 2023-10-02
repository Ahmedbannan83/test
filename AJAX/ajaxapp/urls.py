from django.urls import path
from .views import *

app_name = 'ajaxapp'

urlpatterns = [
    path('', HomeView.as_view(),name="home"),
    path('about/', AboutView.as_view(),name="about"),
    path('all-articles/', AllArticlesView.as_view(),name="all-articles"),
    path('create-article/', CreateArticlesView.as_view(),name="all-articles"),
]