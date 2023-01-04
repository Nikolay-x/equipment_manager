from django.urls import path

from em_asd.spares.views import spares_list, spares_add, SparesEditView, SparesDeleteView

urlpatterns = (
    path('spares_list/', spares_list, name='spares'),
    path('spares/pump/<int:pump_id>/add/', spares_add, name='spares add'),
    path('spares/edit/<int:pk>/', SparesEditView.as_view(), name='spares edit'),
    path('spares/delete/<int:pk>/', SparesDeleteView.as_view(), name='spares delete'),
)
