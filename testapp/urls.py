from django.urls import path
from testapp import views


urlpatterns = [
    path('admin1',views.admin),
    path('lecture/<int:course_id>/',views.assign_lecture),
    path('panel',views.panel),
]