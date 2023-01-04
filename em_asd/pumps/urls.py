from django.urls import path

from em_asd.pumps.views import pumps_list, pump_details, pump_add, PumpEditView, \
    pump_delete, pump_activities, pump_certificates, pump_manuals, pump_spares

urlpatterns = (

    path('pumps_list/', pumps_list, name='pumps list'),
    path('pump/details/<int:pump_id>/', pump_details, name='pump details'),
    path('pump/add/', pump_add, name='pump add'),
    path('pump/edit/<int:pk>/', PumpEditView.as_view(), name='pump edit'),
    path('pump/delete/<int:pump_id>/', pump_delete, name='pump delete'),
    path('pump/<int:pump_id>/acitivities/', pump_activities, name='pump activities'),
    path('pump/<int:pump_id>/certificates/', pump_certificates, name='pump certificates'),
    path('pump/<int:pump_id>/manuals/', pump_manuals, name='pump manuals'),
    path('pump/<int:pump_id>/spares/', pump_spares, name='pump spares'),
)
