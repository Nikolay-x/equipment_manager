from django.urls import path

from em_asd.api.views import PumpsListApiView, CertificatesListApiView, ActivitiesListApiView, ManualsListApiView, \
    SparesListApiView, PumpRUDApiView, PumpsCreateApiView

urlpatterns = (
    path('pumps/', PumpsListApiView.as_view(), name='api list pumps'),
    path('certificates/', CertificatesListApiView.as_view(), name='api list certificates'),
    path('activities/', ActivitiesListApiView.as_view(), name='api list activities'),
    path('manuals/', ManualsListApiView.as_view(), name='api list manuals'),
    path('spares/', SparesListApiView.as_view(), name='api list spares'),
    path('pump_add/', PumpsCreateApiView.as_view(), name='api add pump'),
    path('pump_rud/<int:pk>/', PumpRUDApiView.as_view(), name='api rud pump'),
)
