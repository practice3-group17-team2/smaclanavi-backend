from administer_data import views
from django.urls import path
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_nested import routers

router = routers.SimpleRouter()

router.register(r'class_infos', views.ClassInfoViewSet)
router.register(r'reviews', views.ReviewViewSet)
router.register(r'lec_infos', views.UpcomingLecInfoViewSet, basename='lec_info')

lecinfos_router = routers.NestedSimpleRouter(router, r'lec_infos', lookup='lec_info')
lecinfos_router.register(r'date', views.LecScheduleViewSet, basename='lec_schedule')

urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path(r'', include(router.urls)),
    path(r'', include(lecinfos_router.urls)),
])
