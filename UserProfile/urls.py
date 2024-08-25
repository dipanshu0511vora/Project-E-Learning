from django.urls import path
from .views import grade_list, grade_detail, subjects_list, subjects_detail, userprofile_list, userprofile_detail, video_list, video_detail

urlpatterns = [
    path('grades/', grade_list, name='grade_list'),
    path('grades/<int:pk>/', grade_detail, name='grade_detail'),
    path('subjects/', subjects_list, name='subjects_list'),
    path('subjects/<int:pk>/', subjects_detail, name='subjects_detail'),
    path('userprofiles/', userprofile_list, name='userprofile_list'),
    path('userprofiles/<int:pk>/', userprofile_detail, name='userprofile_detail'),
    path('videos/', video_list, name='video_list'),
    path('videos/<int:pk>/', video_detail, name='video_detail'),
]
