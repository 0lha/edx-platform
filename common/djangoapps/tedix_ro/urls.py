from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from .views import CityViewSet, SchoolViewSet, manage_courses, students_import

router = DefaultRouter()

router.register(r'cities', CityViewSet)
router.register(r'schools', SchoolViewSet)

urlpatterns = [
    url(r'^manage_courses$', manage_courses, name='manage_courses'),
    url(r'^admin/tedix_ro/studentprofile/import/$', students_import, name='students_import'),
    url(r'^api/', include(router.urls))
]
