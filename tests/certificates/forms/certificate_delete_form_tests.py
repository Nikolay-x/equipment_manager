from django.test import TestCase

from em_asd.certificates.forms import CertificateDeleteForm


class CertificateDeleteFormTests(TestCase):
    def test_certificate_delete_form_disabled_fields__when_all__expect_all_to_be_disabled(self):
        form = CertificateDeleteForm()
        disabled_fields = {
            name: field.widget.attrs[CertificateDeleteForm.disabled_attr_name]
            for name, field in form.fields.items()
        }

        self.assertEqual(
            CertificateDeleteForm.disabled_attr_name,
            disabled_fields['name']
        )

        self.assertEqual(
            CertificateDeleteForm.disabled_attr_name,
            disabled_fields['issue_date']
        )

        self.assertEqual(
            CertificateDeleteForm.disabled_attr_name,
            disabled_fields['expiry_date']
        )

        self.assertEqual(
            CertificateDeleteForm.disabled_attr_name,
            disabled_fields['certificate_url']
        )

    def test_certificate_delete_form_readonly_fields__when_all__expect_all_to_be_readonly(self):
        form = CertificateDeleteForm()
        readonly_fields = {
            name: field.widget.attrs[CertificateDeleteForm.readonly_attr_name]
            for name, field in form.fields.items()
        }

        self.assertEqual(
            CertificateDeleteForm.readonly_attr_name,
            readonly_fields['name']
        )

        self.assertEqual(
            CertificateDeleteForm.readonly_attr_name,
            readonly_fields['issue_date']
        )

        self.assertEqual(
            CertificateDeleteForm.readonly_attr_name,
            readonly_fields['expiry_date']
        )

        self.assertEqual(
            CertificateDeleteForm.readonly_attr_name,
            readonly_fields['certificate_url']
        )

    def test_certificate_delete_form_disabled_fields__when_name_is_disabled__expect_name_to_be_disabled(self):
        CertificateDeleteForm.disabled_fields = ('name', )
        form = CertificateDeleteForm()

        disabled_fields = {
            name: field.widget.attrs[CertificateDeleteForm.disabled_attr_name]
            for name, field in form.fields.items()
            if name == 'name' and CertificateDeleteForm.disabled_attr_name in field.widget.attrs
        }

        self.assertEqual(
            CertificateDeleteForm.disabled_attr_name,
            disabled_fields['name'],
        )

        self.assertEqual(1, len(disabled_fields))

    def test_certificate_delete_form_readonly_fields__when_name_is_readonly__expect_name_to_be_readonly(self):
        CertificateDeleteForm.readonly_fields = ('name', )
        form = CertificateDeleteForm()

        readonly_fields = {
            name: field.widget.attrs[CertificateDeleteForm.readonly_attr_name]
            for name, field in form.fields.items()
            if name == 'name' and CertificateDeleteForm.readonly_attr_name in field.widget.attrs
        }

        self.assertEqual(
            CertificateDeleteForm.readonly_attr_name,
            readonly_fields['name'],
        )

        self.assertEqual(1, len(readonly_fields))
