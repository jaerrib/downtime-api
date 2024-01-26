from rest_framework.routers import SimpleRouter

from .views import UserViewSet, LogViewSet

router = SimpleRouter()
router.register("users", UserViewSet, basename="users")
router.register("", LogViewSet, basename="logs")

urlpatterns = router.urls
