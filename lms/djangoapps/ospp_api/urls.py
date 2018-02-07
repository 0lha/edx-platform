from django.conf.urls import url

from ospp_api.views import CreateUserView, EnrollUserView, RoutView

urlpatterns = (
    url(r'^create_user$', CreateUserView.as_view(), name='create_user'),
    url(r'^course_enrollments$', EnrollUserView.as_view(), name='course_enrollments'),
    url(r'^rout_to/(?P<lms_page_name>\w+)/$', RoutView.as_view(), name='rout_to'),
)
