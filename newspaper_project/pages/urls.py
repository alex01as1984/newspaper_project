from django.urls import path

from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(),  name='home'),     # new 2 , method_HomePageView(views) and link_home
]