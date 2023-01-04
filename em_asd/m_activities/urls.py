from django.urls import path

from em_asd.m_activities.views import activities_list, activity_add, ActivityEditView, ActivityDeleteView

urlpatterns = (
    path('activities_list/', activities_list, name='activities'),
    path('activity/pump/<int:pump_id>/add/', activity_add, name='activity add'),
    path('activity/edit/<int:pk>/', ActivityEditView.as_view(), name='activity edit'),
    path('activity/delete/<int:pk>/', ActivityDeleteView.as_view(), name='activity delete'),
)
