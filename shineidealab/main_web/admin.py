from django.contrib import admin

# Register your models here.
from main_web.forms import ContactDataForm
from main_web.models import ReleaseData, ContactData



# release_data
class ReleaseDataAdmin(admin.ModelAdmin):
	list_display = ["__str__", "release_type", "release_created_at"]
	class Meta:
		model = ReleaseData

admin.site.register(ReleaseData, ReleaseDataAdmin)


# ContactData
class ContactDataAdmin(admin.ModelAdmin):
	list_display = ["__str__", "contact_name", "contact_type", "contact_message", "contact_created_at"]
	form = ContactDataForm

admin.site.register(ContactData, ContactDataAdmin)