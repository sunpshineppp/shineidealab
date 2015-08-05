from django.db import models


# Create your models here.

# release
class ReleaseData(models.Model):
    release_title = models.CharField(max_length=100)
    release_content_brief = models.TextField(max_length=500)
    release_photo_brief = models.URLField(max_length=500)
    release_content = models.TextField(max_length=50000)
    release_photo = models.URLField(max_length=500)
    release_type = models.CharField(max_length=100)
    release_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
    	return str(self.release_title)

# contact
class ContactData(models.Model):
	contact_name = models.CharField(u'姓名',max_length=100)
	contact_mail = models.EmailField(u'MAIL',max_length=100)
	contact_type = models.CharField(u'問題種類',max_length=100)
	contact_message = models.TextField(u'留言',max_length=50000)
	contact_created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.contact_mail)