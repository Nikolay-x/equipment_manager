from rest_framework import generics as rest_views

from em_asd.api.serializers import PumpSerializer, CertificateSerializer, ActivitySerializer, ManualSerializer, \
    SparesSerializer, PumpCRUDSerializer
from em_asd.certificates.models import Certificate
from em_asd.m_activities.models import Activity
from em_asd.manuals.models import Manual
from em_asd.pumps.models import Pump
from em_asd.spares.models import Spares


# Create your views here.


class CertificatesListApiView(rest_views.ListCreateAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class ActivitiesListApiView(rest_views.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class ManualsListApiView(rest_views.ListCreateAPIView):
    queryset = Manual.objects.all()
    serializer_class = ManualSerializer


class SparesListApiView(rest_views.ListCreateAPIView):
    queryset = Spares.objects.all()
    serializer_class = SparesSerializer


class PumpsListApiView(rest_views.ListAPIView):
    queryset = Pump.objects.all()
    serializer_class = PumpSerializer

    def get_queryset(self):
        tag = self.request.query_params.get('tag')
        queryset = self.queryset

        if tag:
            queryset = queryset.filter(tag=tag)

        return queryset.all()


class PumpsCreateApiView(rest_views.CreateAPIView):
    queryset = Pump.objects.all()
    serializer_class = PumpCRUDSerializer


class PumpRUDApiView(rest_views.RetrieveUpdateDestroyAPIView):
    queryset = Pump.objects.all()
    serializer_class = PumpCRUDSerializer
