from django.urls import path
from rest_framework.routers import DefaultRouter

from api import views

routers = DefaultRouter()

routers.register("roles", views.RoleViewSet, basename="role")
routers.register("users", views.UserViewSet, basename="user")
routers.register("users-unpaginated", views.UserListViewSet, basename="user")
routers.register("parking-spots", views.ParkingSpotViewSet, basename="parking-spot")
routers.register("reservations", views.ReservationViewSet, basename="reservation")
routers.register(
    "charging-requests", views.ChargingRequestViewSet, basename="charging-request"
)
# router.register('payments', views.PaymentViewSet, basename='payment')
routers.register('user-register', views.UserRegistrationViewSet, basename='register')
urlpatterns = [
    path("login", views.LoginView.as_view()),
    path("logout", views.LogoutView.as_view()),
    path("refresh", views.RefreshView.as_view()),
    path("current", views.CurrentUserView.as_view()),
    path("permissions", views.PermissionListView.as_view()),
]

urlpatterns += routers.urls
