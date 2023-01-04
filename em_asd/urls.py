"""equip_mgmt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('em_asd.api.urls')),

    path('admin/', admin.site.urls),
    path('accounts/', include('em_asd.accounts.urls')),
    path('pumps/', include('em_asd.pumps.urls')),
    path('certificates/', include('em_asd.certificates.urls')),
    path('activities/', include('em_asd.m_activities.urls')),
    path('manuals/', include('em_asd.manuals.urls')),
    path('spares/', include('em_asd.spares.urls')),
    path('', include('em_asd.common.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'em_asd.core.exception_handlers.page_not_found_view'
handler500 = 'em_asd.core.exception_handlers.error_view'
handler403 = 'em_asd.core.exception_handlers.permission_denied_view'
handler400 = 'em_asd.core.exception_handlers.bad_request_view'
