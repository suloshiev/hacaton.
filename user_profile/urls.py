
from user_profile.views import ProfileViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('profile', ProfileViewSet)
router.register('comments',CommentViewSet)

urlpatterns = []
urlpatterns.extend(router.urls)

