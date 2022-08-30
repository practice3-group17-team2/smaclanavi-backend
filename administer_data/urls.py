from django.urls import path
from administer_data import views

urlpatterns = [
    path('classinfo/', views.classinfo_list),
    path('classinfo/<int:pk>/', views.classinfo_detail),
]