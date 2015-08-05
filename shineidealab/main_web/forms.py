from django import forms
from main_web.models import ContactData
from crispy_forms.helper import FormHelper


class ContactDataForm(forms.ModelForm):
	class Meta:
		model = ContactData
		fields = ["contact_mail", "contact_name", "contact_type", "contact_message"]