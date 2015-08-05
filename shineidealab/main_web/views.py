from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages


from main_web.forms import ContactDataForm
from main_web.models import ReleaseData




def page_home(request):   
    # release
    release_list_brief = ReleaseData.objects.all()

    

    # contact
    form = ContactDataForm(request.POST or None)

    if form.is_valid():
      contact_mail = form.cleaned_data.get("contact_mail")
      contact_name = form.cleaned_data.get("contact_name")
      contact_type = form.cleaned_data.get("contact_type")
      contact_message = form.cleaned_data.get("contact_message")

      instance = form.save(commit = False)
      instance.save()

      contact_notice_mail_subject = "%s 您好：謝謝您的留言，將有專人為您服務。"%(contact_name)
      contact_notice_mail_message = """以下是您的留言，將有專人跟您聯絡。  
      需求類型：%s
      留言內容: %s """%(contact_type,contact_message)
      contact_notice_mail_from = settings.EMAIL_HOST_USER
      contact_notice_mail_to = [contact_mail, settings.EMAIL_HOST_USER]

      send_mail(contact_notice_mail_subject,contact_notice_mail_message,contact_notice_mail_from,contact_notice_mail_to,fail_silently=False)

      messages.success(request, '謝謝您的留言，將有專人與您聯繫。')

    # combine all above into context 
    context = {
      "release_list_brief": release_list_brief,
      "form": form
    }

    return render(request,
                  'home.html',
                  context
                  )

def page_about(request):
    return render(request,
                  'about.html',
                  )

def page_projects(request):
    return render(request,
                  'projects.html',
                  )

def page_release(request):

  # release
    release_list_brief = ReleaseData.objects.all()

  # combine all above into context 
    context = {
      "release_list_brief": release_list_brief
    }

    return render(request,
                  'release.html',
                  context
                  )

def page_contact(request):

  # contact
    form = ContactDataForm(request.POST or None)

    if form.is_valid():
      contact_mail = form.cleaned_data.get("contact_mail")
      contact_name = form.cleaned_data.get("contact_name")
      contact_type = form.cleaned_data.get("contact_type")
      contact_message = form.cleaned_data.get("contact_message")

      instance = form.save(commit = False)
      instance.save()

      contact_notice_mail_subject = "%s 您好：謝謝您的留言，將有專人為您服務。"%(contact_name)
      contact_notice_mail_message = """以下是您的留言，將有專人跟您聯絡。  
      需求類型：%s
      留言內容: %s """%(contact_type,contact_message)
      contact_notice_mail_from = settings.EMAIL_HOST_USER
      contact_notice_mail_to = [contact_mail, settings.EMAIL_HOST_USER]

      send_mail(contact_notice_mail_subject,contact_notice_mail_message,contact_notice_mail_from,contact_notice_mail_to,fail_silently=False)

      messages.success(request, '謝謝您的留言，將有專人與您聯繫。')

    # combine all above into context 
    context = {
      "form": form
    }

    return render(request,
                  'contact.html',
                  context
                  )
