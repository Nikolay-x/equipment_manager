from django.urls import path

from em_asd.certificates.views import certificates_list, certificate_add, certificate_delete

urlpatterns = (
    path('certificates_list/', certificates_list, name='certificates'),
    path('certificate/pump/<int:pump_id>/add/', certificate_add, name='certificate add'),
    path('certificate/delete/<int:certificate_id>/', certificate_delete, name='certificate delete'),
)
