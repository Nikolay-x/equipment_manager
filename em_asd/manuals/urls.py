from django.urls import path

from em_asd.manuals.views import manuals_list, manual_add, manual_delete

urlpatterns = (
    path('manuals_list/', manuals_list, name='manuals'),
    path('manual/pump/<int:pump_id>/add/', manual_add, name='manual add'),
    path('manual/delete/<int:manual_id>/', manual_delete, name='manual delete'),
)
