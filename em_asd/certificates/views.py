from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect

from em_asd.certificates.forms import CertificateAddForm, CertificateDeleteForm
from em_asd.certificates.models import Certificate
from em_asd.core.decorators import allow_groups
from em_asd.core.utils import check_if_engineer
from em_asd.pumps.models import Pump


# Create your views here.


@login_required
def certificates_list(request):
    search_item = request.GET.get('pattern', None)

    if search_item:
        valid_certificates = Certificate.objects.filter(expiry_date__gt=datetime.today()) | \
                             Certificate.objects.filter(expiry_date__exact=None)
        valid_certificates = valid_certificates.filter(Q(name__icontains=search_item))

        expired_certificates = Certificate.objects.filter(expiry_date__lte=datetime.today())
        expired_certificates = expired_certificates.filter(Q(name__icontains=search_item))
    else:
        valid_certificates = Certificate.objects.filter(expiry_date__gt=datetime.today()) | \
                             Certificate.objects.filter(expiry_date__exact=None)

        expired_certificates = Certificate.objects.filter(expiry_date__lte=datetime.today())

    engineer = check_if_engineer(request)

    context = {
        'valid_certificates': valid_certificates,
        'expired_certificates': expired_certificates,
        'engineer': engineer,
    }

    return render(request, 'certificates/certificates.html', context)


@login_required
@allow_groups(groups=['Engineer'])
def certificate_add(request, pump_id):
    pump = Pump.objects.filter(pk=pump_id) \
        .get()

    if request.method == 'GET':
        form = CertificateAddForm()
    else:
        form = CertificateAddForm(request.POST)
        if form.is_valid():
            certificate = form.save(commit=False)
            certificate.pump = pump
            form.save()
            return redirect('pumps list')

    context = {
        'form': form,
        'pump_id': pump_id,
    }

    return render(request, 'certificates/certificate_add.html', context)


@login_required
@allow_groups(groups=['Engineer'])
def certificate_delete(request, certificate_id):
    certificate = Certificate.objects.filter(pk=certificate_id).get()

    if request.method == 'GET':
        form = CertificateDeleteForm(instance=certificate)
    else:
        form = CertificateDeleteForm(request.POST, instance=certificate)
        certificate.delete()
        return redirect('certificates')

    context = {
        'form': form,
        'certificate': certificate,
        'certificate_id': certificate_id,
    }

    return render(request, 'certificates/certificate_delete.html', context)
