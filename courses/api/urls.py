from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('courses', views.CourseViewSet)

app_name = 'courses'
urlpatterns = [
    path('subjects/',
         views.SubjectListView.as_view(),
         name='subject_list'),
    path('subjects/<pk>/',
         views.SubjectDetailView.as_view(),
         name='subject_detail'),
    path('courses/<pk>/enroll/',
         views.CourseViewSet.as_view({'post':'create'}),
         name='course_enroll'),
    path('', include(router.urls)),
]
