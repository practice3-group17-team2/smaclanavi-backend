from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from administer_data import views

urlpatterns = [
    path('classinfo/', views.classInfo_list),
    path('classinfo/<int:pk>/', views.classInfo_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)