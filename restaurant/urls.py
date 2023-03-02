# define URL route for index() view
from django.urls import path
from . import views
from .views import BookingView, UserViewSet, SingleMenuItemView, MenuItemView

urlpatterns = [
    path("", views.index, name="index"),
    path("bookings", BookingView.as_view(), name="menu"),
    path("users", UserViewSet.as_view(), name="menu"),
    path("menu/", MenuItemView.as_view(), name="menu"),
    path("menu/<int:pk>", SingleMenuItemView.as_view(), name="menu"),
]
