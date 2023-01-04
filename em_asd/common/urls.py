from django.urls import path

from em_asd.common.views import home_page, about, compressors, generators, oil_separators
from em_asd.core.decorators import allow_groups

urlpatterns = (
    path('', home_page, name='home page'),
    path('about/', about, name='about'),
    path('compressors/', compressors, name='compressors'),
    path('generators/', generators, name='generators'),
    path('oil_separators/', oil_separators, name='oil separators'),
    path('access_denied/', allow_groups, name='access denied'),
)
