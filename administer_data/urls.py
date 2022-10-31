from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from administer_data import views
from rest_framework import routers

router = routers.SimpleRouter()
# (r'lecinfos', )
router.register(r'classinfos', views.ClassInfoViewSet)
router.register(r'reviews', views.ReviewViewSet)
router.register(r'lecinfos', views.UpcomingLecInfoViewSet, basename='lecinfo')

urlpatterns = format_suffix_patterns([
    path('', views.api_root),
])

urlpatterns += router.urls
