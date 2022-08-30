from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from administer_data import views

urlpatterns = [
    path('classinfo/', views.ClassInfoList.as_view()),
    path('classinfo/<int:pk>/', views.ClassInfoDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)