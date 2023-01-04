from rest_framework import serializers

from em_asd.certificates.models import Certificate
from em_asd.m_activities.models import Activity
from em_asd.manuals.models import Manual
from em_asd.pumps.models import Pump
from em_asd.spares.models import Spares


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'


class ManualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manual
        fields = '__all__'


class SparesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spares
        fields = '__all__'


class PumpSerializer(serializers.ModelSerializer):
    certificate_set = CertificateSerializer(many=True)
    activity_set = ActivitySerializer(many=True)
    manual_set = ManualSerializer(many=True)
    spares_set = SparesSerializer(many=True)

    class Meta:
        model = Pump
        fields = '__all__'


class PumpCRUDSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pump
        fields = '__all__'
